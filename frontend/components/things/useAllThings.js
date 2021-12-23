import { gql, useQuery } from '@apollo/client'

export default function useAllThings() {

  const query = useQuery(gql`
    {
      allThings {
        id
        name
        user {
          username
          firstName
          lastName
        }
        widgets {
          shape {
            name
          }
          color {
            name
          }
          number
        }
      }
    }
  `)

  return { query, things: query.data?.allThings || [] }
}