
IO.puts "Hello, " <> "chum."

2 + 3

2 + 3 == 5

String.length("The quick brown fox jumps over the lazy dog")

255

0b0110

0o644

0x1F

3.14

0.14

1.0e-10

true

false

nil

:foo

:foo == :bar

true |> is_atom

:true |> is_boolean

:true === true

is_atom(MyApp.MyModule)

:crypto.rand_bytes 3

"Hello"

"dziekuje"

"foo
> bar"

2 + 2

2 - 1

2 * 5

10 / 5

div(10, 5)

rem(10, 3)

-20 || true

false || 42

42 && true

42 && nil

!42

!false

true and 42

false or true

not false

42 and true

1 > 2

1 != 2

2 == 2

2 <= 3


2 == 2.0

2 === 2.0

:hello > 999

{:hello, :world} > [1, 2, 3]

name = "Sean"
"Hello #{name}"

name = "Sean"
"Hello" <> name

list = [3.14, :pie, "Apple"]
["pi"] ++ list
list ++ ["cherry"]

[1, 2] ++ [3, 4, 1]

["foo", :bar, 42] -- [42, "bar", "foo"]

[1,2,2,3,2,3] -- [1,2,3,2]

hd [3.14, :pie, "Apple"]
tl [3.14, :pie, "Apple"]

[head | tail] = [3.14, :pie, "Apple"]

{3.14, :pie, "Apple"}

File.read("./euler_001.ex1s")

[foo: "bar", hello: "world"]

[{:foo, "bar"}, {:hello, "world"}]

map = %{:foo => "bar", "hello" => :world}

key = "ello"
%{key => "world"}

%{:foo => "bar", :foo => "hello world"}

%{foo: "bar", hello: "world"} == %{:foo => "bar", :hello => "world"}

map = %{foo: "bar", hello: "world"}
map.hello

map = %{foo: "bar", hello: "world"}
%{map | foo: "baz"}
