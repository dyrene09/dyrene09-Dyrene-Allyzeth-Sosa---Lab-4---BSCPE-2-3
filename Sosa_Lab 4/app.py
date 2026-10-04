from flask import Flask, render_template, request

app = Flask(__name__)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        items = []
        current = self.head

        while current:
            items.append(current.data)
            current = current.next

        return items


works_list = LinkedList()
works_list.append({
    'type': 'STRING',
    'title': 'Uppercase Converter',
    'description': 'Convert words or sentences into uppercase using Python.',
    'url': 'uppercase'
})
works_list.append({
    'type': 'MATHEMATICS',
    'title': 'Area of a Circle',
    'description': 'Calculate the area of a circle by entering its radius.',
    'url': 'circle'
})
works_list.append({
    'type': 'MATHEMATICS',
    'title': 'Area of a Triangle',
    'description': 'Calculate the area of a triangle using its base and height.',
    'url': 'triangle'
})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/works')
def works():
    return render_template('works.html', works=works_list.to_list())


@app.route('/works/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None

    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()

    return render_template('touppercase.html', result=result)


@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    error = None

    if request.method == 'POST':
        radius = request.form.get('radius', '')

        try:
            radius = float(radius)
            if radius <= 0:
                error = 'Please enter a number greater than zero.'
            else:
                result = 3.14 * radius * radius
        except ValueError:
            error = 'Please enter a valid number.'

    return render_template('circle.html', result=result, error=error)


@app.route('/works/area/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    error = None

    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')

        try:
            base = float(base)
            height = float(height)

            if base <= 0 or height <= 0:
                error = 'Please enter numbers greater than zero.'
            else:
                result = 0.5 * base * height
        except ValueError:
            error = 'Please enter valid numbers.'

    return render_template('triangle.html', result=result, error=error)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
