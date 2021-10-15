<template>
  <div id="app">
    <div v-if="!login">
      <p>
        <label>Username: </label>
        <input type="text" v-model="username">
      </p>
      <p>
        <label>Password: </label>
        <input type="password" v-model="password">
      </p>
      <button @click="do_login">Login</button>
    </div>
    <div v-if="login">
      <h3>Persons</h3>
    <ul>
      <li v-for="person in persons" :key="person.id">
        {{ person.name }}
      </li>
    </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      persons: null,
      username: '',
      password: '',
      login: false,
      token: null
    }
  },
  methods: {
    get_persons() {
      axios.get('http://localhost:8000/api/persons',{
        headers: {
          'Authorization': `Bearer ${this.token}`
        }
      })
      .then(response => (this.persons = response.data))
    },
    do_login() {
       axios.post('http://localhost:8000/api/token/', {
        'username': this.username,
        'password': this.password
      })
      .then(response => {
        this.token = response.data.access
        this.login = true
        this.get_persons()
      })
    }
  }
}
</script>

<style>
</style>
