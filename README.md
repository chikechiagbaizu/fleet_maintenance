# Service Fleet & Maintenance Manager

An Odoo module for tracking physical assets (laptops, vehicles, machinery) and keeping their maintenance on schedule. Each asset has a service history, a service interval, and a computed next-service date, so overdue maintenance is visible at a glance.

## Features

- **Asset register**: name, type (laptop, vehicle, machinery), and responsible employee.
- **Vehicle-only fields**: license plate is shown only when the asset type is Vehicle.
- **Service history**: each asset has a list of service records (date, type, description, cost, technician, state). Deleting an asset deletes its service records.
- **Preventative maintenance**
  - Each asset has a service interval in days.
  - Last service date comes from the latest completed service.
  - Next service date = last service date + interval.
  - Overdue assets are flagged and can be filtered in the list view.
- **Views**: form, list, kanban and search views, with Overdue and By Type filters.
- **Role-based access**
  - **Fleet Managers**: full access to all assets and services.
  - **Regular users**: read-only access to assets assigned to them.

## Models

| Model | Purpose |
|---|---|
| `fleet.asset` | The asset and its maintenance schedule |
| `fleet.service` | A single planned or completed service on an asset |

## Installation

1. Copy `fleet_maintenance` into your Odoo `addons` path.
2. Restart the server and update the Apps list.
3. Install **Service Fleet & Maintenance Manager** (depends on `base` and `hr`).

To apply updates:

```
odoo -d <your_db> -u fleet_maintenance --stop-after-init
```

## Usage

1. Create an asset, set its type, responsible employee and service interval.
2. Add service records in the asset's Service History tab.
3. Mark a service as Done. The asset's last and next service dates update automatically.
4. Use the Overdue filter in the asset list to see what needs attention.

## Requirements

- Odoo 19.0
- Depends on `hr`; no external Python dependencies

## License

LGPL-3

## Author

Chike Chiagbaizu