
## Executing Python Code

Type the following code in the body of an Outline node

```python
@language python

import sys
import os
g.es(os.environ['QTLIB'])
g.es(sys.version)
```

Press CTRL+B to execute code. 

**If nothing is selected, entire body will be executed.**

You can also select the Outline node and click the ``script-button`` below the ``File Menu`` to create an executable button in the user interface.
