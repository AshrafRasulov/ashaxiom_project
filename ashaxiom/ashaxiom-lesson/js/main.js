/**
 * AshAxiom Academy SPA Engine v3.5
 * Features: Deep-Folder Merged Localization & Dynamic Counter
 */

let academyState = {
    currentModule: '',  // basic_math, visualization, etc.
    lessons: [],        // lesson list
    currentIndex: -1    // current position
};

// 1. ДВИЖОК-СКАНЕР (Discovery)
async function discoverLessons(folder) {
    try {
        const response = await fetch(`pages/${folder}/`);
        const html = await response.text();
        const regex = /href="(lesson\d+\.html)"/g;
        let found = [];
        let match;
        while ((match = regex.exec(html)) !== null) found.push(match[1]);
        // Сортировка: lesson01, lesson02...
        return found.sort((a, b) => a.localeCompare(b, undefined, {numeric: true}));
    } catch (err) { return []; }
}

// 2. УНИВЕРСАЛЬНЫЙ ДВИЖОК ПЕРЕВОДА (Deep Merge Logic)
async function applyTranslations() {
    const lang = localStorage.getItem('ash_lang') || 'RU'; // RU по умолчанию
    const flag = localStorage.getItem('ash_flag') || 'Ru.png';
    const langLower = lang.toLowerCase();

    try {
        // --- ШАГ А: Загрузка глобального JSON (Header, Footer, Levels) ---
        const globalRes = await fetch(`lang/${lang.toUpperCase()}.json`);
        let translations = await globalRes.json();

        // --- ШАГ Б: Поиск локального JSON (Внутри папки модуля) ---
        if (academyState.currentModule) {
            try {
                // Путь: lang/trading/ru.json
                const localRes = await fetch(`lang/${academyState.currentModule}/${langLower}.json`);
                if (localRes.ok) {
                    const localTr = await localRes.json();
                    // Сливаем объекты: локальные ключи имеют приоритет
                    translations = { ...translations, ...localTr };
                }
            } catch (e) {
                console.log("[Translation] No local file for this module.");
            }
        }

        // --- ШАГ В: Обновление UI ---
        document.querySelectorAll('[data-lang]').forEach(el => {
            const key = el.getAttribute('data-lang');
            
            // Динамическая подстановка для уроков (lXX_title -> l01_title)
            let finalKey = key;
            if (key.includes('lXX')) {
                const num = (academyState.currentIndex + 1).toString().padStart(2, '0');
                finalKey = key.replace('XX', num);
            }

            if (translations[finalKey]) {
                // Если это кнопка или инпут с атрибутом value
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = translations[finalKey];
                } else {
                    el.innerText = translations[finalKey];
                }
            }
        });

        // --- ШАГ Г: Установка счетчика (data-lesson-num) ---
        document.querySelectorAll('[data-lesson-num]').forEach(el => {
            el.innerText = academyState.currentIndex + 1;
        });

        // --- ШАГ Д: Обновление селектора языка в Navbar ---
        if (document.getElementById('currentLangFlag')) 
            document.getElementById('currentLangFlag').src = `img/${flag}`;
        if (document.getElementById('currentLangName')) 
            document.getElementById('currentLangName').innerText = lang;

    } catch (err) {
        console.error("[Translation Engine Error]:", err);
    }
}

// 3. ФУНКЦИЯ СМЕНЫ ЯЗЫКА
function changeLang(lang, flag) {
    localStorage.setItem('ash_lang', lang);
    localStorage.setItem('ash_flag', flag);
    console.log(`[Language] Switched to ${lang}`);
    applyTranslations(); // Мгновенно обновляем все тексты на текущей странице
}

// 4. ДВИЖОК НАВИГАЦИИ
async function navigate(route) {
    const root = document.getElementById('app-root');
    let targetFile = 'home_fragment.html';

    // Закрытие мобильного меню при клике
    const navbar = document.getElementById('navbarNav');
    if (navbar && navbar.classList.contains('show')) {
        const bsCollapse = new bootstrap.Collapse(navbar);
        bsCollapse.hide();
    }

    if (route === 'home' || !route) {
        academyState = { currentModule: '', lessons: [], currentIndex: -1 };
    } 
    else if (route === 'prev' || route === 'next') {
        const step = (route === 'next') ? 1 : -1;
        const newIdx = academyState.currentIndex + step;
        
        if (newIdx < 0 || newIdx >= academyState.lessons.length) {
            targetFile = 'home_fragment.html';
            academyState = { currentModule: '', lessons: [], currentIndex: -1 };
        } else {
            academyState.currentIndex = newIdx;
            targetFile = `pages/${academyState.currentModule}/${academyState.lessons[newIdx]}`;
        }
    } 
    else {
        // Вход в модуль (карточки или Dropdown)
        const sorted = await discoverLessons(route);
        if (sorted.length > 0) {
            academyState.currentModule = route;
            academyState.lessons = sorted;
            academyState.currentIndex = 0;
            targetFile = `pages/${route}/${sorted[0]}`;
        } else if (route.startsWith('train')) {
            targetFile = `additional/${route}.html`;
        }
    }

    try {
        const response = await fetch(targetFile);
        if (!response.ok) throw new Error("404");
        root.innerHTML = await response.text();
        window.location.hash = route;
        applyTranslations(); // Применяем переводы к новому контенту
        window.scrollTo(0, 0);
    } catch (err) {
        console.error("[SPA] Route failed:", route);
        navigate('home');
    }
}

// 5. СТАРТ
window.addEventListener('DOMContentLoaded', () => {
    const r = window.location.hash.replace('#', '') || 'home';
    navigate(r);
});

window.addEventListener('hashchange', () => {
    const r = window.location.hash.replace('#', '');
    if (r !== 'next' && r !== 'prev') navigate(r);
});