 const n1 = 3; // global variable

        function hello() {
            var n2 = 5; // an internal variable of a function

            if (n2>0) {
                const n3 = 8; // an internal variable of a block
                var n4 = 9; // an internal variable of a function
            }
            console.log(n1); // global variable is visible everywhere
            console.log(n2); // the internal variable is aviailable inside the function
            //console.log(n3); -- an internal variable of a block is not available outside the function
            console.log(n4); // the internal variable of the function is available inside the function

        }

        hello();

        console.log(n1);