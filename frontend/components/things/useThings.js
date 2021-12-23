import React from 'react'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useThings() {

  const query = useQuery(
    'things', () => axios.get('/api/v1/things/').then(response => response.data)
  )

  const things = query.data ? query.data : []

  return { query, things }
}