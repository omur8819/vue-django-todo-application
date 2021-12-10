<template>
  <div id="app" class="container max-w-md">
    <Todo title="My List"/>
  </div>
</template>

<script>
import Todo from '@/components/Todo'

export default {
  name: 'App',

  components: {
    Todo
  }
}
</script>

<style>
@import '../node_modules/bulma';
#app {
  @apply mx-auto text-center;
}

h1 {
  @apply text-2xl font-bold;
}
</style>
