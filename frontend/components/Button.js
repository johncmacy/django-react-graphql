import React from "react"

export default function Button({ text, className, onClick }) {
  return (
    <button type="button" className={className} onClick={onClick}>{text}</button>
  )
}