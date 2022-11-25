<template>
  <div id="app">
    <h1>진화 단계 가이드</h1>
    <router-link :to="{ name: 'home' }">
      <button>Home</button>
    </router-link>
    <router-link :to="{ name: 'happeed' }">
      <button>Start</button>
    </router-link>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
