📦 Ansible Role: app — Deploy Flask Application with Gunicorn
📌 الهدف من الرول

هذه الرول مصممة لنشر مشروع Flask (Back-End) فقط على سيرفر لينكس باستخدام:

    Python virtual environment (venv)

    Gunicorn كـ WSGI server

    systemd لتشغيل الخدمة تلقائيًا

    ⚠️ هذه الرول لا تتعامل مع الواجهة الأمامية (Front-End) أو Nginx مباشرة. يُفضل استخدامها فقط مع تطبيق Flask مسؤول عن الـ API أو صفحات HTML بسيطة.

🧠 متى تستخدم هذه الرول؟

    عند نشر مشروع Flask جديد.

    عند إعادة نشر مشروع تم تعديله.

    عند ترحيل مشروع Flask إلى سيرفر جديد.

    في أي سيناريو يكون فيه التطبيق هو Back-End فقط ويتصل بقاعدة بيانات أو يقدم صفحات HTML عبر Jinja2.

🔁 كيفية إعادة استخدام الرول

كل ما عليك هو تغيير قيم المتغيرات في الملف vars/main.yml:

app_name: votingsystem      # اسم مجلد المشروع واسم خدمة systemd
app_entry: app              # اسم ملف Python الأساسي (بدون .py)
app_dir: "/opt/{{ app_name }}"
venv_dir: "{{ app_dir }}/venv"

ثم:

    تأكد أن مشروعك (الذي يحتوي على app.py, requirements.txt, templates, static) موجود داخل مجلد بنفس اسم app_name.

    شغّل الـ playbook على السيرفر:

    ansible-playbook site.yml -l app1

📂 هيكل المشروع المطلوب

افترض أن app_name: votingsystem

votingsystem/
├── app.py              ← هذا هو app_entry
├── requirements.txt
├── static/
└── templates/

📜 ما الذي تفعله هذه الرول بالتحديد؟

    ترفع مجلد المشروع بالكامل إلى /opt/{{ app_name }}

    تنشئ virtual environment داخل هذا المسار

    تثبّت جميع الـ dependencies من requirements.txt داخل venv

    تثبّت Gunicorn داخل venv

    تجهز ملف systemd لتشغيل الخدمة تلقائيًا

    تشغل الخدمة باسم {{ app_name }}.service

💡 أمثلة للاستخدام المستقبلي
✅ مشروع تصويت بسيط

    back-end فقط

    Flask API + HTML

    استخدم هذه الرول

❌ مشروع Front-End Angular

    لا تستخدم هذه الرول

    استخدم رول خاصة بـ nginx أو static hosting

✅ مشروع Flask API

    بدون HTML

    يقدم JSON responses

    استخدم هذه الرول

🔄 كيف تحدث الرول لمشروع جديد؟

    غير app_name, app_entry حسب مشروعك الجديد.

    تأكد إنك حطيت فولدر المشروع الجديد بنفس اسم app_name في نفس مكان الـ playbook.

    شغل الـ playbook.

هل تحب أضيف مثال عملي لمشروع pollsapp جوه نفس الرول كمرجع تجريبي؟
