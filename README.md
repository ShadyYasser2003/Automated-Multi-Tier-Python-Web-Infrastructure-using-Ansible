# 🗳️ Automated Multi-Tier Python Voting App Infrastructure using Ansible

This project sets up a complete **multi-tier web application** for voting using **Ansible**. The system consists of three VMs configured automatically:

- 🧱 **Backend**: Python Flask app with Gunicorn
- 🌐 **Frontend**: Static HTML/CSS/JS served by Nginx
- 🗄️ **Database**: MySQL for storing votes
- 💾 **Backup & Monitoring**: Auto-daily DB backup and simple MySQL service monitor

---

## ⚙️ Project Structure

```bash
.
├── Vagrantfile
├── site.yml
├── roles/
│   ├── app/        # Flask backend setup
│   ├── db/         # MySQL DB setup
│   ├── frontend/   # Nginx frontend setup
│   ├── backup/     # DB backup cron
│   └── monitor/    # MySQL service monitoring
└── frontend/       # Static frontend files
    ├── index.html
    ├── script.js
    └── style.css
```

---

## 🖥️ Virtual Machine Setup (Vagrant)

| VM     | Role       | IP Address      |
|--------|------------|-----------------|
| db1    | Database   | `192.168.59.13` |
| app1   | Backend    | `192.168.59.12` |
| web1   | Frontend   | `192.168.59.11` |

To start the VMs:

```bash
vagrant up
```

---

## 🚀 How It Works

1. **`app1`** runs the Flask app behind Gunicorn and listens on port `5000`
2. **`db1`** runs MySQL and stores vote results
3. **`web1`** hosts static HTML/JS that communicates with the backend through `/api/` via Nginx reverse proxy
4. Backups of the DB are created daily under `/opt/db_backups` via cron
5. Monitoring script checks MySQL every 5 minutes

---

## 🔧 Usage

### To provision infrastructure:

```bash
ansible-playbook -i inventory site.yml
```

### To access the app:

Open in browser:
```http
http://192.168.59.11
```

---

## 🛠️ Reusability

This project is designed to be reusable for any Flask-based backend + static frontend by:

- Editing the app files in `roles/app/files/flaskapp`
- Replacing frontend files in `frontend/`
- Customizing `voteapp.conf` for Nginx if needed

---

## 📦 Roles Overview

| Role      | Description                                     |
|-----------|-------------------------------------------------|
| `app`     | Flask app deployment with Gunicorn + systemd    |
| `frontend`| Serve static files via Nginx                    |
| `db`      | Install + configure MySQL                       |
| `backup`  | Schedule daily `mysqldump` backups via cron     |
| `monitor` | Monitor MySQL service and alert if down         |





