import React from 'react'
import useThings from './useThings'

export default function ThingList() {
  const { query, things } = useThings()

  return (
    <div>
      {query.isFetching ? 'loading...' : null}
      {things.map(thing => <div key={thing.id}>{thing.color}</div>)}
    </div>
  )
}