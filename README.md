[Project screenshots](https://github.com/Mesnyankin/django_todo/issues/1)

<b>Project idea.</b><br>
We will develop To-Do List – a web application for task management.<br>
Users will be able to:
<ul>
 <li>Register and log in</li>
 <li>Create, edit, delete tasks</li>
 <li>Set reminders (using Redis for cache)</li>
 <li>See the task list in a convenient interface</li>
</ul>

<b>Project structure:</b><br>
<ul>
 <li>Django – core web application</li>
 <li>PostgreSQL – database</li>
 <li>Redis – caching</li>
 <li>Gunicorn – WSGI server for running Django</li>
 <li>Nginx – proxy server for handling requests</li>
 <li>Docker & Docker Compose – containerization of all components</li>
</ul>
