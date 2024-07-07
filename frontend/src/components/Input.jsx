import React from 'react';
import classNames from 'classnames';

export const Input = React.forwardRef(({ className, ...props }, ref) => {
  return (
    <input
      ref={ref}
      className={classNames(
        'block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
        className
      )}
      {...props}
    />
  );
});

Input.displayName = 'Input';
