import {
  ApolloClient, ApolloProvider, InMemoryCache
} from "@apollo/client"
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8080/api/',
  cache: new InMemoryCache(),
})

ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
  , document.getElementById('root')
)
