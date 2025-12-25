/**
 * AshAxiom SPA Engine v2.0
 */

// 1. УМНАЯ ЛОГИКА ПУТЕЙ
function getFilePath(route) {
    if (route === 'home' || !route) return 'home_fragment.html';
    if (route.startsWith('lesson')) return `pages/${route}.html`;
    if (route.startsWith('train')) return `additional/${route}.html`;
    return 'home_fragment.html';
}

// 2. ДВИЖОК НАВИГАЦИИ
async function navigate(route) {
    const root = document.getElementById('app-root');
    const targetFile = getFilePath(route);

    try {
        const response = await fetch(targetFile);
        if (!response.ok) throw new Error("Page not found");
        const html = await response.text();
        
        root.innerHTML = html;
        window.location.hash = route;
        
        // После загрузки HTML применяем перевод
        applyTranslations();
        // Скроллим в начало
        window.scrollTo(0, 0);
    } catch (err) {
        console.error("Navigation error:", err);
        navigate('home');
    }
}

// 3. ДВИЖОК ПЕРЕВОДА
async function applyTranslations() {
    const lang = localStorage.getItem('ash_lang') || 'ENG';
    const flagFileName = localStorage.getItem('ash_flag') || 'Eng.png';

    try {
        const response = await fetch(`lang/${lang}.json`);
        const translations = await response.json();

        document.querySelectorAll('[data-lang]').forEach(el => {
            const key = el.getAttribute('data-lang');
            if (translations[key]) el.innerText = translations[key];
        });

        // Обновляем кнопку выбора языка
        if (document.getElementById('currentLangFlag')) 
            document.getElementById('currentLangFlag').src = `img/${flagFileName}`;
        if (document.getElementById('currentLangName')) 
            document.getElementById('currentLangName').innerText = lang;

    } catch (err) {
        console.warn("Translation failed, check JSON files.");
    }
}

function changeLang(lang, flag) {
    localStorage.setItem('ash_lang', lang);
    localStorage.setItem('ash_flag', flag);
    applyTranslations();
}

// 4. СТАРТ ПРИ ЗАГРУЗКЕ
window.addEventListener('DOMContentLoaded', () => {
    const initialRoute = window.location.hash.replace('#', '') || 'home';
    navigate(initialRoute);
});

// Слушаем изменение хеша (кнопки назад/вперед в браузере)
window.addEventListener('hashchange', () => {
    const route = window.location.hash.replace('#', '');
    navigate(route);
});