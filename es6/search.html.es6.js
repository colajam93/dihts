        window.onload = function () {
            ['{{ for }}', '{{ in }}', '{{ match }}'].forEach(i => {
                document.getElementById(i + '_radio').checked = true;
                document.getElementById(i + '_label').className += ' active';
            });
            document.getElementById('keyword').value = '{{ keyword }}';
        };
        function move_page(page) {
            document.getElementById('page').value = page;
            const form = document.getElementById('f');
            form.submit()
        }

