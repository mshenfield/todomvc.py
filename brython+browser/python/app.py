"""TodoMVC Brython."""
from browser import (
    document,
    html as H,
)
from browser.local_storage import storage
import json


class App(H.SECTION):
    def __init__(self, state):
        super().__init__(
            [
                Header(),
                Main(state.todos, state.toggle_all, state.filter),
                Footer(state.todos, state.filter)
            ],
            Class='todoapp',
            id='todoapp',
        )


class Header(H.HEADER):
    def __init__(self):
        super().__init__(
            [
                H.H1('todos'),
                NewTodoInput(),
            ],
            Class='header',
        )



class NewTodoInput(H.INPUT):
    def __init__(self):
        super().__init__(
            Class='new-todo',
            placeholder='What needs to be done?',
        )
        self.bind('keyup', self.on_keyup)

    def on_keyup(self, event):
        """Generates a new Todo from the text in our input, skipping empty strings"""
        todo_text = self.value.strip()
        make_new_todo = event.key == 'Enter' and todo_text
        if make_new_todo:
            self.value = ''
            def update(state):
                state.todos.append(Todo(todo_text))
            update_state(update)


ACTIVE_FILTER = 'active'
ALL_FILTER = ''
COMPLETED_FILTER = 'completed'


class Main(H.SECTION):
    def __init__(self, todos, toggle_all=False, filter=ALL_FILTER):
        todos = todos
        if filter == ACTIVE_FILTER:
            todos = [t for t in todos if not t.completed]
        elif filter == COMPLETED_FILTER:
            todos = [t for t in todos if t.completed]

        super().__init__(
            [
                ToggleAllInput(toggle_all),
                H.LABEL(
                    'Mark all as complete',
                    For='toggle-all',
                ),
                TodoList(todos),
            ],
            Class='main',
            style={'display': 'block' if len(todos) else 'none'},
        )


class ToggleAllInput(H.INPUT):
    def __init__(self, toggle_all):
        super().__init__(
            Class='toggle-all',
            checked=toggle_all,
            id='toggle-all',
            type='checkbox',
        )
        self.toggle_all = toggle_all
        self.bind('click', self.toggle)

    def toggle(self, event):
        def update(state):
            state.toggle_all = not self.toggle_all
            for t in state.todos:
                t.completed = state.toggle_all

        update_state(update)


class Footer(H.HEADER):
    def __init__(self, todos, filter):
        count = len([todo for todo in todos if not todo.completed])
        item_text = 'item' if count == 1 else 'items'

        super().__init__(
            [
                H.SPAN(
                    [
                        H.STRONG(count),
                        ' {} left'.format(item_text),
                    ],
                    Class='todo-count',
                ),
                H.UL(
                    [
                        H.LI(
                            FilterLink('All', filter=ALL_FILTER, current_filter=filter),
                        ),
                        H.LI(
                            FilterLink('Active', filter=ACTIVE_FILTER, current_filter=filter),
                        ),
                        H.LI(
                            FilterLink('Completed', filter=COMPLETED_FILTER, current_filter=filter),
                        ),
                    ],
                    Class='filters',
                ),
                ClearCompletedButton(todos),
            ],
            Class='footer',
            style={'display': 'block' if len(todos) else 'none'},
        )


class FilterLink(H.A):
    def __init__(self, text, filter, current_filter):
        self.filter = filter
        super().__init__(
            text,
            Class='selected' if current_filter == filter else None,
            href='#/{}'.format(self.filter),
        )
        self.bind('click', self.set_filter)

    def set_filter(self, event):
        def update(state):
            state.filter = self.filter
        update_state(update)


class ClearCompletedButton(H.BUTTON):
    def __init__(self, todos):
        completed_todos = [
            todo for todo in todos
            if todo.completed
        ]

        super().__init__(
            'Clear completed',
            Class='clear-completed',
            style={'display': 'default' if completed_todos else 'none'},
        )
        self.bind('click', self.clear_completed)

    def clear_completed(self, event):
        def update(state):
            state.todos = [
                todo for todo in state.todos
                if not todo.completed
            ]
        update_state(update)


class TodoList(H.UL):
    def __init__(self, todos):
        super().__init__(
            [TodoElement(todo) for todo in todos],
            Class='todo-list',
        )


class TodoElement(H.LI):
    def __init__(self, todo):
        classes = []
        if todo.completed:
            classes.append('completed')
        if todo.editing:
            classes.append('editing')

        super().__init__(
            [
                H.DIV(
                    [
                        TodoCheckbox(todo),
                        TodoEditingLabel(todo),
                        TodoDestroy(todo),
                    ],
                    Class='view',
                ),
                TodoEditor(todo),
            ],
            Class=' '.join(classes),
        )


class TodoEditingLabel(H.LABEL):
    def __init__(self, todo):
        self.todo = todo
        super().__init__(todo.text)
        self.bind('dblclick', self.activate_editing)

    def activate_editing(self, event):
        def update(state):
            self.todo.editing = True
        update_state(update)


class TodoEditor(H.INPUT):
    def __init__(self, todo):
        self.todo = todo
        super().__init__(
            Class='edit',
            value=todo.text,
        )
        self.bind('blur', self.on_blur)
        self.bind('keyup', self.on_keyup)

    def on_blur(self, event):
        self._save_editor()

    def on_keyup(self, event):
        if event.key == 'Enter':
            self._save_editor()

    def _save_editor(self):
        todo_text = self.value.strip()
        def update(state):
            if todo_text:
                self.todo.text = todo_text
                self.todo.editing = False
            else:
                state.todos = [
                    todo for todo in state.todos
                    if todo is not self.todo
                ]
        update_state(update)


class TodoCheckbox(H.INPUT):
    def __init__(self, todo):
        super().__init__(
            Class='toggle',
            checked=todo.completed,
            type='checkbox',
        )
        self.todo = todo
        self.bind('click', self.on_click)

    def on_click(self, event):
        checked = event.target.checked
        def update(state):
            self.todo.completed = checked
        update_state(update)



class TodoDestroy(H.BUTTON):
    def __init__(self, todo):
        super().__init__(
            Class='destroy'
        )

        self.todo = todo
        self.bind('click', self.on_click)

    def on_click(self, event):
        def update(state):
            state.todos = [
                todo for todo in state.todos
                if todo is not self.todo
            ]
        update_state(update)


class Todo:
    """An item in a todo list."""
    def __init__(self, text='', completed=False):
        self.text = text
        self.completed = completed
        self.editing = False

    def store(self):
        return {
            'text': self.text,
            'completed': self.completed,
        }

class State:
    def __init__(
        self,
        new_todo_text='',
        todos=None,
        toggle_all=False,
        filter=ALL_FILTER,
    ):
        self.new_todo_text = new_todo_text
        self.todos = todos or []
        self.toggle_all = toggle_all
        self.filter = filter


    @classmethod
    def from_storage(cls):
        state = cls()
        print('checking')
        if 'todoapp' in storage:
            print('loading')
            stored_state = json.loads(storage['todoapp'])
            state.new_todo_text = stored_state['new_todo_text']
            state.todos = [Todo(**todo_dict) for todo_dict in stored_state['todos']]
            state.toggle_all = stored_state['toggle_all']
            state.filter = stored_state['filter']
        return state

    def store(self):
        print('storing')
        storage['todoapp'] = json.dumps({
            'new_todo_text': self.new_todo_text,
            'todos': [todo.store() for todo in self.todos],
            'toggle_all': self.toggle_all,
            'filter': self.filter,
        })
        print(storage['todoapp'])


state = State.from_storage()


def update_state(updater):
    global state
    updater(state)
    state.store()
    document['todoapp'].remove()
    document.body.prepend(App(state))


update_state(lambda s: s)
