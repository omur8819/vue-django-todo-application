<template>
  <div>
    <h1 class="title mt-10">My Todo List</h1>
    <div class="mt-10">
      <input
        type="text"
        data-testid="todo-input"
        placeholder="Add todo item..."
        class="border border-gray-300 p-1 text-blue-700"
        id="input-tag"
        v-model="newTodo"
      >
      <button
        class="px-3 py-1 text-white bg-blue-500 mb-4"
        id="button-tag"
        data-testid="todo-submit"
        @click.prevent="addTodo">Add
      </button>
    </div>
    <ul data-testid="todos" class="text-left mt-10">
      <li
        v-for="(todo, todoKey) of todos"
        :data-testid="`todo-${todoKey}`"
        :key="todoKey"
        class="block mb-3"
        id="card-tag"
      >
        {{ todo.description }}
      </li>
    </ul>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
  name: 'Todo',

  props: {
    title: {
      type: String,
      required: true
    }
  },

  data () {
    return {
      todos: [],
      newTodo: ''
    }
  },
  mounted () {
    this.getTodos()
  },
  methods: {
    addTodo () {
      if (this.newTodo) {
        getAPI.post('tasks/', { description: this.newTodo })
          .then(response => {
            this.todos.push({
              description: this.newTodo,
              done: false
            })
            this.newTodo = ''
          })  
          .catch(err => console.log(`err`, err))
      }
    },
    getTodos() {
      getAPI.get('tasks/',)
      .then(response => this.todos = response.data)
      .catch(err => console.log(`err`, err))     
    }
  }

}
</script>
<style lang="css">
html, 
body, 
.home { 
  width: 100vw;
  min-height: 100vh;
  background-color: #eeeeee;
  overflow-x:hidden;
}
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
.title {
  text-align: center;
  color: #00c4a7;
}
#input-tag {
  border-radius: 10px;
}
#button-tag {
  border-radius: 10px;
}

#card-tag {
  border: 5px solid #00c4a7;
  text-align: center;
  border-radius: 5px;
  font-size: 25px;
  background-color: #00c4a7;
  color: white;
}

</style>
