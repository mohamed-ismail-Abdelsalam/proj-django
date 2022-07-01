/////////////////// for images //////////////////////
        let $btns= $(".projects_section .buttons button");
            $btns.click(function(e){
                $(".projects_section .buttons button").removeClass("active");
                e.target.classList.add("active");
                let selector = $(e.target).attr('data-filter');
                $(".projects_section .grid").isotope({
                    filter : selector
                });
                return false ;
            });
            //$(".projects_section .buttons #btn1").trigger("click");///
            $('.projects_section .test-popup-link').magnificPopup({
            type: 'image',
            gallery:{enabled:true}

        });