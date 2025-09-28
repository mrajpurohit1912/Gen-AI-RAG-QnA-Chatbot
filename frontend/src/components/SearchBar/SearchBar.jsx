import React from 'react'
import './SearchBar.css'

const SearchBar = ({value,onChange}) => {
  return (
    <div className='search-container'>
      <input type='text' placeholder='Ask your queries...' className='search-input' value={value} onChange={(e) => onChange(e.target.value)}/> 
    </div>
  )
}

export default SearchBar
