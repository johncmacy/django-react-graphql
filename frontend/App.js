import React from 'react'
import { QueryClient, QueryClientProvider } from 'react-query'
import { ReactQueryDevtools } from 'react-query/devtools'
import Button from './components/Button'
import ThingList from './components/things/ThingList'

export default function App() {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        refetchOnWindowFocus: false,
      }
    }
  })

  return (
    <QueryClientProvider client={queryClient}>
      <div>
        <h1>App</h1>
        <a href="/profile">Profile</a>
        <a href="/login">Login</a>
        <a href="/logout">Logout</a>
        <Button text="Test" onClick={(e) => alert("hello")} />

        <ThingList />
      </div>

      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  )
}