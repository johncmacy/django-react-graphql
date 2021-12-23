import React from 'react'
import ThingList from './components/things/ThingList'

export default function App() {
  return (
    <div>
      <h1>App</h1>
      <nav style={{ display: 'flex', gap: '1em' }}>
        <a href="/profile">Profile</a>
        <a href="/api">API</a>
        <a href="/login">Login</a>
        <a href="/logout">Logout</a>
        <a href="/admin">Admin</a>
      </nav>

      <hr />

      <ThingList />
    </div>
  )
}