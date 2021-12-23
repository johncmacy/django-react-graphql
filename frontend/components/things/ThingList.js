import React from 'react'
import useAllThings from './useAllThings'

export default function ThingList() {
  const { query, things } = useAllThings()

  return (
    <div>
      {query.isFetching ? 'loading...' : null}
      {things.map(thing =>
        <ul key={thing.id}>
          <li>
            {`${thing.user.firstName}'s ${thing.name}`}

            <ul>
              {thing.widgets.map(
                widget =>
                  <li key={widget.id}>
                    {`${widget.number} ${widget.color.name} ${widget.shape.name}(s)`}
                  </li>)}
            </ul>
          </li>
        </ul>)}
    </div>
  )
}