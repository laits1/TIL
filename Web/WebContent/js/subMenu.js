/* subMenu.js */

// 메인 메뉴의 전체보기 클릭했을 때 모든 메뉴 항목 보이게

$(function() {
$('#showAllMenu').on('click',function(){
    if($(this).text()=='전체보기 ▼') {
        $('.subMenuItem').slideDown(1000);

        $('#subMenuBox').css('visibility', 'visible');
        // 전체보기는 숨겨져 있는 상태이므로 visible로 변경
        $(this).text('메뉴닫기 ▲').css('color','blue');
        // 메뉴 text를 메뉴 닫기로 변경

    } else {
        $('.subMenuItem').slideUp(1);
        // 메뉴 닫기 이므로 메뉴 속성을 hidden으로 변경
        $('#subMenuBox').css('visibility', 'hidden');
        // 메뉴 text를 전체보기로 변경
        $(this).text('전체보기 ▼').css('color','black');
    }

});



});     // ready 함수 종료
