const state = () => {
  return {
    list: [

    ],
  }
}

const getters = {
}
const mutations = {
  ON_IS_COMPLETED(state, todo) {
    const idx = state.list.indexOf(todo)
    state.list[idx].isCompleted = !state.list[idx].isCompleted
  },
  ON_IS_Important(state, todo) {
    const idx = state.list.indexOf(todo)
    state.list[idx].isImportant = !state.list[idx].isImportant
  },
  ON_TODO_INPUT(state, newTodo) {
    state.list.push(newTodo)
  }
}
const actions = {
  OnIsCompleted(context, todo) {
    context.commit('ON_IS_COMPLETED', todo)
  },
  OnIsImportant(context, todo) {
    context.commit('ON_IS_Important', todo)
  },
  OnTodoInput(context, todo) {
    const newTodo = {
      id: Date.now(),
      content: todo.input,
      dueDateTime: new Date(),
      isCompleted: false,
      isImportant: todo.isImportant,
    }
    context.commit('ON_TODO_INPUT', newTodo)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
}