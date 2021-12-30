import React, { Component } from 'react';
import SimpleKeyboard from 'react-simple-keyboard';
import 'react-simple-keyboard/build/css/index.css';

function Keyboard() {   
    return (
        <SimpleKeyboard
            physicalKeyboardHighlight: {false};
        />
    );
}

export default Keyboard;