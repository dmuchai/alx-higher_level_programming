#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Prints the rectangle using the character X
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Exchanges the width and height of the rectangle
  rotate () {
    if (this.width && this.height) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  // Doubles the width and height of the rectangle
  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
