## Reporting Issues

Please report an issue with as many details as possible by
[opening a new issue](https://github.com/pearkes/stripe-hooks/issues/new).
Thank you!

## Tests

If you'd like to change something, feel free to do so and
submit a pull request. **Tests are appreciated but not required**.
I'm happy to write them.

## Development Environment

There are two options that will work.

### VM Development

You'll need [Vagrant](http://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/).

    $ git clone ...
    ...
    $ vagrant up
    ...
    $ vagrant ssh
    ...
    $ make deps
    ...
    $ cp .env.example .env
    ...
    $ make run

### Own Machine Development

    $ make deps
    ...
    $ gem install foreman
    ...
    $ cp .env.example .env
    ...
    $ foreman run python app.py
    ...

You'll also need `libevent`. You can install it with brew on OS X or via
your favorite package manager on Linux.

I recommend running it in a VM.
