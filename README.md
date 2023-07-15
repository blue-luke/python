# Notes

I am initialising the airport with planes that stay attached to the airport

# Description

Airport challenge in python

I use pytest, with tests and source files in /

Test files must start with test_ and test functions must start with test_

You can TDD your way to an app

Planes can land and take off

You can't land twice in succession

You can land a plane via an airport

Airports have capacity

I was in the process of defining a full airport and not letting additional planes land. This conflicts with the notion of capacity, as I had initialised an airport with 'capacity' number of ladnded plane, so I couldn't create the surplus plane that the test would need

# python Airport Challenge: 

We have a request from a client to write the software to control the flow of planes at an airport. The planes can land and take off provided that the weather is sunny. Occasionally it may be stormy, in which case no planes can land or take off. Here are the user stories that we worked out in collaboration with the client:

As an air traffic controller 
So I can get passengers to a destination 
I want to instruct a plane to land at an airport

As an air traffic controller 
So I can get passengers on the way to their destination 
I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport

As an air traffic controller 
To ensure safety 
I want to prevent landing when the airport is full 

As the system designer
So that the software can be used for many different airports
I would like a default airport capacity that can be overridden as appropriate

As an air traffic controller 
To ensure safety 
I want to prevent takeoff when weather is stormy 

As an air traffic controller 
To ensure safety 
I want to prevent landing when weather is stormy 
Your task is to test drive the creation of a set of classes/modules to satisfy all the above user stories. You will need to use a random number generator to set the weather (it is normally sunny but on rare occasions it may be stormy). In your tests, you'll need to use a stub to override random weather to ensure consistent test behaviour.

Your code should defend against edge cases such as inconsistent states of the system ensuring that planes can only take off from airports they are in; planes that are already flying cannot take off and/or be in an airport; planes that are landed cannot land again and must be in an airport, etc.

For overriding random weather behaviour, please read the documentation to learn how to use test doubles: https://www.relishapp.com/rspec/rspec-mocks/docs . There’s an example of using a test double to test a die that’s relevant to testing random weather in the test.

Please create separate files for every class, module and test suite.

In code review we'll be hoping to see:

All tests passing
High Test coverage (>95% is good)
The code is elegant: every class has a clear responsibility, methods are short etc.
Reviewers will potentially be using this code review rubric. Referring to this rubric in advance will make the challenge somewhat easier. You should be the judge of how much challenge you want this at this moment.

BONUS

Write an RSpec feature test that lands and takes off a number of planes
Note that is a practice 'tech test' of the kinds that employers use to screen developer applicants. More detailed submission requirements/guidelines are in CONTRIBUTING.md

Finally, don’t overcomplicate things. This task isn’t as hard as it may seem at first.

Submit a pull request early.

Finally, please submit a pull request before Monday at 9am with your solution or partial solution. However much or little amount of code you wrote please please please submit a pull request before Monday at 9am.