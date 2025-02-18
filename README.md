# Minclude

Remove unneeded include directives from your C/C++ source base similar to
[include-what-you-use](http://include-what-you-use.org/). Instead of requiring Clang though,
Minclude uses the naive approach by simply testing which includes can be removed without breaking
the build. The advantages of this are that you can use it with any kind of build tool or
compiler.

Minclude is written in Python 3, you can install it via Python's package manager:

```
pip3 install minclude
```

Now navigate to your source directory and run `minclude` to get started.

## F.A.Q.

### Isn't this - like - super slow?

Yes it is! Depending on the size of your code base, this might take several hours to complete.

### How can I tell Minclude to ignore some include directives?

By default all includes with the following comment are excluded:

```c
#include <string> // IWYU pragma: keep
```

If you want to exclude all system includes instead:

```sh
minclude --exclude_includes "#\s*include\s*<[^>]*>"
```
