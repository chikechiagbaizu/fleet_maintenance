# Project 1: Service Fleet & Maintenance Manager 🚛🛠️

An enterprise-grade asset tracking and preventative maintenance compliance module custom-built for the Odoo ecosystem. 

## 📋 Business Case & Problem Statement
Companies managing physical operations infrastructure (logistics vans, construction tools, high-capacity machinery) lose substantial revenue due to unpredicted equipment down-time and operational decay. This breakdown typically happens because organizations lack an integrated, auditable framework to track preventative maintenance and schedule routine services.

**The Solution:** This module implements a robust asset lifecycle log tracking engine. It bridges field operations with human resources by tying equipment management to responsible operators, enforcing preventative service logs, and providing structural data security grids to maintain database integrity.

---

## 🛠️ Key Technical Implementations
* **Custom Dynamic Relational Architecture:** Built a bidirectional relational link mapping a parent vehicle profile (`fleet.asset`) down to its historical sub-lines (`fleet.service`) using an optimized `One2many` dataset bridge with automated transactional cascade deletes.
* **Modern UI UX Layout Engineering:** Developed advanced Form, List, and interactive Kanban views matching the modern Odoo 17+ client framework specs (utilizing the new `<list>` grid layout paradigm).
* **Conditional Client-Side Form Modifiers:** Implemented dynamic field visibility constraints using optimized evaluation strings (`invisible="asset_type != 'vehicle'"`) to adjust field states on the interface in real-time based on selected data matrices.
* **Rigorous Multilayer Access Control:** Locked down system access parameters using row-level security boundaries (`ir.rule`) and group-level data access profiles (`ir.model.access.csv`), restricting regular employees to a read-only baseline for specific equipment classifications (`machinery`).

---

## 🗂️ Module Directory Structure
```text
fleet_maintenance/
├── __manifest__.py                  # Module descriptor and data load order definition
├── __init__.py                      # Python package initializers
├── models/
│   ├── __init__.py
│   ├── fleet_asset.py               # Core persistent model data structures
│   └── fleet_service.py             # Relational service logs model
├── security/
│   ├── ir.model.access.csv          # Matrix configuration for Group-level CRUD permissions
│   └── fleet_security_rules.xml     # Row-level record rules (ir.rule) for data isolation
└── views/
    ├── fleet_asset_views.xml        # Form, List, and Window Action UI configurations
    └── menu.xml                     # Global navigation menu hierarchy layout
```

---

## 🔩 Technical Specifications & Code Snippets

### Data Architecture (Python ORM Models)
```python
class FleetAsset(models.Model):
    _name = 'fleet.asset'
    _description = 'Fleet Asset'

    name = fields.Char(string='Tracking Name', required=True)
    asset_type = fields.Selection([
        ('laptop', 'Laptop'),
        ('vehicle', 'Vehicle'),
        ('machinery', 'Industrial Machinery'),
    ], string='Asset Type', required=True)
    assigned_employee_id = fields.Many2one('hr.employee', string='Responsible Employee')
    service_history_ids = fields.One2many('fleet.service', 'asset_id', string='Service History')
```

### High-Density Data Security Configuration
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_fleet_asset_manager,fleet.asset,model_fleet_asset,base.group_system,1,1,1,1
access_fleet_asset_user,fleet.asset,model_fleet_asset,base.group_user,1,0,0,0
```

---

## 🚀 Deployment & Installation Checklist
1. Place the module folder inside your Odoo `custom_addons` directory path.
2. Ensure dependencies (`hr` for employee management) are present in your target database.
3. Update the Odoo configuration or manifest index via the dashboard interface (*Apps -> Update Apps List*).
4. Install `fleet_maintenance`. Test permissions by logging in under a non-administrative account assigned to the standard `Internal User` group (`base.group_user`) to verify that the row-level restriction locks act cleanly on the postgres execution layer.
