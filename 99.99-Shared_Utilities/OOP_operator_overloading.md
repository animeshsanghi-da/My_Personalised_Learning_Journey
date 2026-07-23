Here is a comprehensive list of all the magic (dunder) methods used for operator overloading in Python, categorized by their functionality.

### 1. Comparison Operators

These methods allow you to define custom logic for comparing objects. They must return a boolean value (`True` or `False`).

|Operator|Syntax|Magic Method|
|---|---|---|
|`<`|`obj1 < obj2`|`__lt__(self, other)`|
|`<=`|`obj1 <= obj2`|`__le__(self, other)`|
|`==`|`obj1 == obj2`|`__eq__(self, other)`|
|`!=`|`obj1 != obj2`|`__ne__(self, other)`|
|`>`|`obj1 > obj2`|`__gt__(self, other)`|
|`>=`|`obj1 >= obj2`|`__ge__(self, other)`|

### 2. Binary Arithmetic Operators

These methods overload standard mathematical operations when your custom object is on the **left side** of the operator.

|Operator|Syntax|Magic Method|
|---|---|---|
|`+`|`obj1 + obj2`|`__add__(self, other)`|
|`-`|`obj1 - obj2`|`__sub__(self, other)`|
|`*`|`obj1 * obj2`|`__mul__(self, other)`|
|`/`|`obj1 / obj2`|`__truediv__(self, other)`|
|`//`|`obj1 // obj2`|`__floordiv__(self, other)`|
|`%`|`obj1 % obj2`|`__mod__(self, other)`|
|`**`|`obj1 ** obj2`|`__pow__(self, other)`|
|`@`|`obj1 @ obj2`|`__matmul__(self, other)` _(Matrix Multiplication)_|
|`divmod()`|`divmod(obj1, obj2)`|`__divmod__(self, other)`|

### 3. Reflected (Right-Hand) Arithmetic Operators

These methods are called if the left operand does not support the corresponding operation and the operands are of different types. They allow your custom object to be on the **right side** of the operator.

|Operator|Syntax|Magic Method|
|---|---|---|
|`+`|`other + self`|`__radd__(self, other)`|
|`-`|`other - self`|`__rsub__(self, other)`|
|`*`|`other * self`|`__rmul__(self, other)`|
|`/`|`other / self`|`__rtruediv__(self, other)`|
|`//`|`other // self`|`__rfloordiv__(self, other)`|
|`%`|`other % self`|`__rmod__(self, other)`|
|`**`|`other ** self`|`__rpow__(self, other)`|
|`@`|`other @ self`|`__rmatmul__(self, other)`|

### 4. Augmented Assignment Operators

These methods overload the in-place arithmetic assignments (combining an operation with assignment).

|Operator|Syntax|Magic Method|
|---|---|---|
|`+=`|`obj1 += obj2`|`__iadd__(self, other)`|
|`-=`|`obj1 -= obj2`|`__isub__(self, other)`|
|`*=`|`obj1 *= obj2`|`__imul__(self, other)`|
|`/=`|`obj1 /= obj2`|`__itruediv__(self, other)`|
|`//=`|`obj1 //= obj2`|`__ifloordiv__(self, other)`|
|`%=`|`obj1 %= obj2`|`__imod__(self, other)`|
|`**=`|`obj1 **= obj2`|`__ipow__(self, other)`|
|`@=`|`obj1 @= obj2`|`__imatmul__(self, other)`|

### 5. Bitwise Operators

These handle bit-level manipulations and logical boolean operations on objects.

|Operator|Syntax|Magic Method|
|---|---|---|
|`&`|`obj1 & obj2`|`__and__(self, other)`|
|`\|`|`obj1 \| obj2`|`__or__(self, other)`|
|`^`|`obj1 ^ obj2`|`__xor__(self, other)`|
|`<<`|`obj1 << obj2`|`__lshift__(self, other)`|
|`>>`|`obj1 >> obj2`|`__rshift__(self, other)`|

_(Note: Bitwise operators also have reflected equivalents like `__rand__`, `__ror__`, etc., and augmented equivalents like `__iand__`, `__ior__`, etc.)_

### 6. Unary Operators

These operators act on a single operand (the object itself).

| Operator | Syntax     | Magic Method       | Description             |
| -------- | ---------- | ------------------ | ----------------------- |
| `-`      | `-obj`     | `__neg__(self)`    | Unary minus / Negation  |
| `+`      | `+obj`     | `__pos__(self)`    | Unary plus              |
| `~`      | `~obj`     | `__invert__(self)` | Bitwise inversion / NOT |
| `abs()`  | `abs(obj)` | `__abs__(self)`    | Absolute value          |