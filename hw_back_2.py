from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
cars = [
    {"id": i, "name": f"Car {i}", "year": str(2010 + (i % 15))}
    for i in range(1, 101)
]

users = [
    {
        "id": 1,
        "email": "aibek@test.com",
        "first_name": "Aibek",
        "last_name": "Bekturov",
        "username": "deadly_knight95"
    },
    {
        "id": 2,
        "email": "maria@test.com",
        "first_name": "Maria",
        "last_name": "Sidorova",
        "username": "masha_88"
    },
    {
        "id": 3,
        "email": "ivan@test.com",
        "first_name": "Ivan",
        "last_name": "Petrov",
        "username": "ivan_p"
    },
    {
        "id": 4,
        "email": "elena@test.com",
        "first_name": "Elena",
        "last_name": "Smirnova",
        "username": "lenka_s"
    },
    {
        "id": 5,
        "email": "alex@test.com",
        "first_name": "Alexey",
        "last_name": "Ivanov",
        "username": "alex_i"
    },
    {
        "id": 6,
        "email": "olga@test.com",
        "first_name": "Olga",
        "last_name": "Vasilyeva",
        "username": "olga_v"
    },
    {
        "id": 7,
        "email": "dmitry@test.com",
        "first_name": "Dmitry",
        "last_name": "Kozlov",
        "username": "dima_k"
    },
    {
        "id": 8,
        "email": "anna@test.com",
        "first_name": "Anna",
        "last_name": "Morozova",
        "username": "anna_m"
    },
    {
        "id": 9,
        "email": "sergey@test.com",
        "first_name": "Sergey",
        "last_name": "Novikov",
        "username": "sergey_n"
    },
    {
        "id": 10,
        "email": "tatiana@test.com",
        "first_name": "Tatiana",
        "last_name": "Sokolova",
        "username": "tatiana_s"
    },
]

@app.route('/cars')
def get_cars():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    if page < 1:
        page = 1
    if limit < 1:
        limit = 10
    
    start = (page - 1) * limit
    end = start + limit
    
    paginated_cars = cars[start:end]
    
    return jsonify({
        'page': page,
        'limit': limit,
        'total': len(cars),
        'total_pages': (len(cars) + limit - 1) // limit,
        'data': paginated_cars
    })


@app.route('/cars/<int:car_id>')
def get_car_by_id(car_id):
    for car in cars:
        if car['id'] == car_id:
            return jsonify(car)
    
    return "Not found", 404


# usres all


USERS_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Users List</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        a { text-decoration: none; color: #2196F3; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>📋 Users List</h1>
    <table>
        <thead>
            <tr><th>ID</th><th>Username</th><th>Full Name</th><th>Email</th></tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td><a href="/users/{{ user.id }}">{{ user.first_name }} {{ user.last_name }}</a></td>
                <td>{{ user.email }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route('/users')
def get_all_users():
    return render_template_string(USERS_TEMPLATE, users=users)


# user id

USER_DETAIL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ user.first_name }} {{ user.last_name }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            max-width: 500px;
            margin: 0 auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 { color: #333; }
        .field { margin: 10px 0; }
        .label { font-weight: bold; color: #555; }
        .value { margin-left: 10px; }
        .back-link { display: block; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>{{ user.first_name }} {{ user.last_name }}</h1>
        <div class="field">
            <span class="label">ID:</span>
            <span class="value">{{ user.id }}</span>
        </div>
        <div class="field">
            <span class="label">Username:</span>
            <span class="value">{{ user.username }}</span>
        </div>
        <div class="field">
            <span class="label">Email:</span>
            <span class="value">{{ user.email }}</span>
        </div>
        <div class="field">
            <span class="label">First Name:</span>
            <span class="value">{{ user.first_name }}</span>
        </div>
        <div class="field">
            <span class="label">Last Name:</span>
            <span class="value">{{ user.last_name }}</span>
        </div>
        <a href="/users" class="back-link">← Back to all users</a>
    </div>
</body>
</html>
"""

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return render_template_string(USER_DETAIL_TEMPLATE, user=user)
    
    return "User not found", 404

#pagination

USERS_PAGINATED_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Users List (with Pagination)</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        a { text-decoration: none; color: #2196F3; }
        a:hover { text-decoration: underline; }
        .pagination {
            margin-top: 20px;
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
        }
        .pagination a, .pagination span {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .pagination a {
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
        }
        .pagination a:hover {
            background-color: #45a049;
        }
        .pagination .current {
            background-color: #333;
            color: white;
            border-color: #333;
        }
        .controls {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            align-items: center;
        }
        select, input[type="submit"] {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        input[type="submit"] {
            background-color: #2196F3;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>📋 Users List (with Pagination)</h1>
    
    <div class="controls">
        <form method="get" style="display: flex; gap: 10px; align-items: center;">
            <label>Items per page:</label>
            <select name="limit" onchange="this.form.submit()">
                <option value="5" {{ 'selected' if limit == 5 else '' }}>5</option>
                <option value="10" {{ 'selected' if limit == 10 else '' }}>10</option>
                <option value="20" {{ 'selected' if limit == 20 else '' }}>20</option>
                <option value="50" {{ 'selected' if limit == 50 else '' }}>50</option>
            </select>
            <input type="hidden" name="page" value="{{ page }}">
        </form>
    </div>
    
    <table>
        <thead>
            <tr><th>ID</th><th>Username</th><th>Full Name</th><th>Email</th></tr>
        </thead>
        <tbody>
            {% for user in paginated_users %}
            <tr>
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td><a href="/users/{{ user.id }}">{{ user.first_name }} {{ user.last_name }}</a></td>
                <td>{{ user.email }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <div class="pagination">
        {% if page > 1 %}
            <a href="?page=1&limit={{ limit }}">⏮ First</a>
            <a href="?page={{ page - 1 }}&limit={{ limit }}">◀ Previous</a>
        {% else %}
            <span class="disabled">⏮ First</span>
            <span class="disabled">◀ Previous</span>
        {% endif %}
        
        {% for p in range(1, total_pages + 1) %}
            {% if p == page %}
                <span class="current">{{ p }}</span>
            {% elif p <= 10 or p > total_pages - 5 %}
                <a href="?page={{ p }}&limit={{ limit }}">{{ p }}</a>
            {% elif p == 11 %}
                <span>...</span>
            {% endif %}
        {% endfor %}
        
        {% if page < total_pages %}
            <a href="?page={{ page + 1 }}&limit={{ limit }}">Next ▶</a>
            <a href="?page={{ total_pages }}&limit={{ limit }}">Last ⏭</a>
        {% else %}
            <span class="disabled">Next ▶</span>
            <span class="disabled">Last ⏭</span>
        {% endif %}
    </div>
    
    <p>Showing {{ start + 1 }} - {{ end if end <= total else total }} of {{ total }} users</p>
</body>
</html>
"""

@app.route('/users-paginated')
def get_users_paginated():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    if page < 1:
        page = 1
    if limit < 1:
        limit = 10
    
    start = (page - 1) * limit
    end = start + limit
    total = len(users)
    total_pages = (total + limit - 1) // limit
    
    paginated_users = users[start:end]
    
    return render_template_string(
        USERS_PAGINATED_TEMPLATE,
        users=users,
        paginated_users=paginated_users,
        page=page,
        limit=limit,
        start=start,
        end=end,
        total=total,
        total_pages=total_pages
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
