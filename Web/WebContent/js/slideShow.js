/* slideShow.js */

$(function() {
    // 이동한 이미지의 index 값 저장 (현재 화면에서 보여지는 이미지의 index)
    var movedIndex = 0;

    // 슬라이드 패널을 움직여주는 함수

    function moveSlide(index) {
        // 전달받은 index 값을 moveIndex에 저장
        movedIndex = index;
        
        // 슬라이드 이동
        var moveLeft =- (index * 1280);
        $('#slidePanel').animate({'left':moveLeft}, 'slow')
    }

    //prev 버튼 클릭하면 앞으로 이동
    $('#prevButton').on('click', function(){	
        if(movedIndex != 0) //첫번째가 아니라면 
            movedIndex = movedIndex - 1; //인덱스 값 -1				
        
        moveSlide(movedIndex); //인덱스값 전달
    });
    
    //next 버튼 클릭하면 뒤로 이동
    $('#nextButton').on('click', function(){	
        if(movedIndex != 4) //마지막이 아니라면 
            movedIndex = movedIndex + 1; //인덱스 값 +1
        
        moveSlide(movedIndex); //인덱스값 전달			
    });

    $('.controlButton').each(function(index) {
        $(this).hover(
            function() {
                $(this).attr('src', 'image/controlButton2.png');
            },
            function() {
                $(this).attr('src', 'image/controlButton1.png');
            }
        );      // hover 종료
    // 클릭 하면 현재 인덱스 값을 moveSlide() 함수에 전달
        $(this).on('click', function() {
            moveSlide(index);
            
        });

    });     // each 끝

    // 초기 슬라이더 위치 랜덤하게 지정
    var randomNumber = Math.floor(Math.random() * 5);
    moveSlide(randomNumber);

});