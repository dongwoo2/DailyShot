import React from 'react';

const Button = ({ label, onClick }) => {
  const buttonStyle = {
    backgroundColor: '#61dafb',
    border: 'none',
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
    borderRadius: '5px',
  };

  return (
    <button style={buttonStyle} onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;
