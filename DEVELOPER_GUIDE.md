
*Deep-dive for system developers.*

```markdown
# AshAxiom Developer Guide (FullReload Architecture)

## 1. Object Spawning Principle
To ensure data integrity and prevent cross-contamination in multi-asset analysis, `BrainCore.solve()` now **spawns** a new instance of `AxiomMain` for every operation.
- **Stateless:** The Brain does not hold intermediate search results.
- **Independent:** Each line in a chart is a unique memory object with its own styling.

## 2. Capsule Expansion (The /update Folder)
AshAxiom is infinitely updateable. To add a new AI capability (e.g., Voice AI or Image AI):
1. Place the external library folder inside `brain/update/`.
2. Create a `<skill_name>.json` passport file defining triggers and entry points.
3. (Optional) Create a `<skill_name>_config.py` adapter to bridge data to the Golden Standard.

## 3. Data Flow Pipeline
- **Fetch**: Expert retrieves raw data from books or APIs.
- **Standardize**: `DataConverter` flattens data into 1D/2D arrays.
- **Visualize**: `hGraph` applies styles and renders synchronized views.

## 4. The Golden Standard Protocol
All methods in new library additions must strictly use:
`def my_method(self, expr=None, var='x', val=0, data=None, ticker=None):`
This ensures the Brain's argument mapper correctly routes user input to your code.