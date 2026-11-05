"""Flask Queue Simulator"""
import os
import secrets
from flask import (Flask, render_template, request, redirect,
                   url_for, session, flash)
from queue_model import Queue

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)


@app.route('/')
def index():
    queue = Queue(session.get('queue', []))
    return render_template(
        'index.html',
        items=queue.items,
        size=queue.size(),
        front=queue.peek(),
        rear=queue.rear(),
        removed=session.get('dequeued', []),
        highlight=request.args.get('peek') == '1'
    )


@app.route('/queue', methods=['POST'])
def operate():
    action = request.form.get('action', '')
    value = request.form.get('value', '').strip()
    queue = Queue(session.get('queue', []))
    removed = session.get('dequeued', [])
    peek = False

    if action == 'enqueue':
        if not value:
            flash('Input is blank. Enter 1 to 24 characters.', 'warning')
        elif len(value) > 24:
            flash('Input is too long (24 characters maximum).', 'warning')
        elif queue.size() >= 20:
            flash('The queue is full (20 items maximum).', 'warning')
        else:
            queue.enqueue(value)
            flash(f'Enqueued {value} at the rear.', 'success')
    elif action == 'dequeue':
        if queue.is_empty():
            flash('The queue is empty. Nothing to dequeue.', 'warning')
        else:
            front = queue.dequeue()
            removed.append(front)
            removed = removed[-20:]
            flash(f'Dequeued {front} from the front.', 'success')
    elif action == 'peek':
        if queue.is_empty():
            flash('The queue is empty. Nothing to peek.', 'warning')
        else:
            peek = True
            flash(f'Front value: {queue.peek()}.', 'info')
    elif action == 'clear':
        queue.clear()
        removed = []
        flash('Queue cleared.', 'info')
    else:
        flash('Unknown action.', 'warning')

    session['queue'] = queue.items
    session['dequeued'] = removed
    if peek:
        return redirect(url_for('index', peek=1))
    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=5001)