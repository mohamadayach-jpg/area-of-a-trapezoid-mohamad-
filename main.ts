// Created by :Mohamad Ayach
// Created on :May 6,2026
// This program calculates the area of a trapezoid by asking the user for the measures of base 1, base 2, and the height. It then calculates and displays the area of the trapezoid.
// 
game.splash("lets calculate the area of a trapezoid")
let base_1 = game.askForNumber("what is base 1 (cm)")
let base_2 = game.askForNumber("what is base 2 (cm)")
let height = game.askForNumber("what is height (cm)")
let area = (base_1 + base_2) / 2 * height
game.splash("the area of the trapezoid with base 1 " + base_1 + "cm and base 2 " + base_2 + "cm and height" + height + "cm is " + area + "cm^2")
