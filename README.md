# Project Two - Virtual Robot Treasure Hunt

The task we decided to implement was the Level 3 scenario. The scenario's requirements were to set up a number of landmarks, a set of traffic lights with instructions and a number of treasures. The two robots, each with a random starting point should collect different treasures that are worth at least 100 points before reaching their given landmark, whilst avoiding each other, moving away from the landmarks with no treasures and following the traffic light instructions. This process occurs until one of the robots has found its treasure first. Furthermore the information about the landmark should be displayed on the screen, as the robot approaches the landmark. 

In our interpretation of the specification we decided to have 4 treasures which would randomly spawn at different landmarks. The robots would randomly spawn and move towards the treasure. If the robot was in a green light zone it would continue, in an amber light zone it would slow down and in a red light zone it would stop. The four light zones change every 3 seconds until both robots have found their two treasures. The robot would only find the treasure by having its x and y coordinates match the landmark where the treasure was located. Once the treasure was found, the treasure would be cleared and the landmark would turn from green to amber indicating that it had been visited by one of the robots. The robots would continue to find treasure until it had found two treasures, and then the robot’s timer would stop. The main program timer would only stop when both robots have found their two treasures.

## Installation
 
TODO: Describe the installation process
 
## Usage
 
TODO: Write usage instructions
 
## Credits
 
TODO: Write credits
 
## License
 
The MIT License (MIT)

Copyright (c) 2015 Sloths

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
