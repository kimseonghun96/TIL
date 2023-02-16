# SCSS

### 설치

- `npm install sass -g` SCSS 설치 커멘드
- `npm show sass version` SCSS 버전 확인

### 플러그인

- SCSS에 작성을 하게 되면 자동으로 컴파일되어 css 파일 생성을 도와주는 기능
- **Live Sass Compiler**

### style.css.map

- 소스맵(SourceMap) 파일
- 컴파일된 소스를 원본 소스로 매핑해 주는 역할

## 기능 및 특징

### 1. 중첩

- before

```css
.header-grand-parent{ color : red; }
.header-grand-parent .header-parent{ color : orange; }
.header-grand-parent .header-parent .header-child{ color : blue; } 
```

- after

```scss
.header-grand-parent{
    color : red;

    .header-parent{
        color : orange;

        .header-child{
            color : blue;
        }
    }
}
```

### 2. 부모참조(&)

- before

```css
.accordion {
  max-width: 600px;
  margin: 4rem auto;
  width: 90%;
  font-family: "Raleway", sans-serif;
  background: #f4f4f4;

  &__copy {
    display: none;
    padding: 1rem 1.5rem 2rem 1.5rem;
    color: gray;
    line-height: 1.6;
    font-size: 14px;
    font-weight: 500;

    &--open {
      display: block;
    }
  }
}
```

- after

```scss
.accordion {
  max-width: 600px;
  margin: 4rem auto;
  width: 90%;
  font-family: "Raleway", sans-serif;
  background: #f4f4f4;
}

.accordion__copy{
    display: none;
    padding: 1rem 1.5rem 2rem 1.5rem;
    color: gray;
    line-height: 1.6;
    font-size: 14px;
    font-weight: 500;
}

.accordion__copy--open{
    display: block;
}
```

- `&`가 컴파일되면서 부모 선택자로 치환되는 것이므로, `& span` / `&span` / `&.span` 은 각각 다르게 취급됨.

```scss
.hello {
  & span {
    color: blue;
  }

  &span {
    color: green;
  }

  &.span {
    color: purple;
  }
}

/** result
1 .hello span
2 .hellospan
3 .hello.span
*/
```

### 3. @mixin & include

- 정의
  
  - 공통 속성들을 모아 정리하고 include로 불러와 사용

- 사용방법
  
  - `@mixin 이름{ ... }` 으로 공통으로 쓸 속성을 적어두고 `@incldue mixin` 이름 으로 불러와서 사용
  - 인자를 주는 방법
  
  ```scss
  @mixin set-color($color, $bg-color){
    color: $color;
    background-color: $bg-color;
  }
  h1{ @include set-color(#FFF, #000); }
  - 일부인자에 기본값을 주거나 특정인자만 따로넘기는 방법
  
  @mixin bg($name, $path: "images/", $format: "png"){
    background-image: url("#{path}#{name},#{format}");
  }
  .logo{ @include bg(logo); }
  .arrow{ @include bg(arrow); }
  ```
  
  - `@if`와 같은 문을 mixin 속에 포함시켜 쓰는 방법
    (믹스인은 stylesheet의 최상위 레벨에서 사용 하므로 가능)
    
    ```scss
    @mixin button($size, $radius: 0) {
      width: $size;
      height: $size;
    
      @if $radius != 0 { border-radius: $radius; }
    }
    .btn-square { @include button(100px); }
    .btn-circle { @include button(100px, $radius: 50%); }
    ```
  
  - `@content`(믹스인에 내용 덧붙이기) `@include`를 이용해 mixin을 불러온 뒤 내용을 추가입력 가능
    
    - ex) 자주쓰는 미디어쿼리 분기문을 만들고, 다른곳에서 불러와쓰는 용도로 사용
    - ex) 접근성을 위한 자주 쓰이는 디자인(대체 텍스트 표시, 말줄임 처리)를 CSS 컴포넌트화화는 데 사용
    
    ```scss
    @mixin hover{
      &:hover{
        // 1) 먼저, 믹스인을 만들고
        font-weight: bold;
        @content;
      }
      &.on{ @content }
    }
    
    button {
      // 2) 불러와 쓸 때 내용을 입력합니다.
      @include hover { color: red; }
    }
    
    // Break Point
    $tablet: 768px;
    $mobile: 540px;
    
    // Tablet
    @mixin res--tablet {
      @media screen and (min-width: #{$tablet}) {
        @content;
      }
    }
    
    // Mobile
    @mixin res--mobile {
      @media screen and (max-width: #{$mobile}) {
        @content;
      }
    }
    .title {
      font-size: 16px;
    
      @include res--tablet { font-size: 14px; }
      @include res--mobile { font-size: 12px; }
    }
    
        * 출력(CSS):
        .title { font-size: 16px; }
        @media screen and (min-width: 768px) {
          .title { font-size: 14px; }
        }
    
        @media screen and (max-width: 540px) {
          .title { font-size: 12px; }
        }
    ```

### 4. @extend(확장기능)

- 정의
  
  - 이미 존재하는 셀렉터(를 `@extend`로 지정해두고 기본 내용을 덧붙일 때 사용
  - ex) [모든 버튼]은 폰트가 굵고 보더가 있지만, 클래스에 따라 보더 색상이 다를 때, 공통되는 부분을 `@extend`(폰트굴게, 보더있음 속성을 가진 button)로 불러오고 추가 css(보더 색상)를 작성
  - `%(placeholder)` : extend할 껍데기로 지정(컴파일 되면 사라짐)
  
  ```scss
  .%button {
    font-weight: bold;
    border-width: 1px;
  }
  
  .button-confirm {
    @extend .button;
    border-color: blue;
  }
  
  .button-error {
    @extend .button;
    border-color: red;
  }
  ```

### 5. extend VS mixin

- @extend
  - 연관성 있는 셀렉터들을 묶어 관리할 수 있음
  - 미디어쿼리 등으로 셀렉터가 묶일 수 없다면 쓸 수 없음
- @mixin
  - 인자를 넣을 수 있음
  - 선택자 관리가 쉬워서 전역으로 쓰기 편함
  - 컴파일된 CSS가 길어지는 단점이 있음

<aside>
💡 선택자끼리 의미론적 관계가 있다면 @extend를,
그렇지 않고 단순히 속성만 겹치는 관계라면 @mixin을 쓰는 것을 추천

</aside>

# 주의사항

- 주석(//)은 컴파일 되면 사라짐
- 변수 재할당 시 이전내용 바꾸지 않음
- 변수에서 하이픈(-)과 언더스코어(_)는 동일하게 취급
- 문자열이나 셀렉터 등에 변수 사용하기 위해서는 보간법(#{}) 사용
- 문자열을 감싼 문자열을 감싼 따옴표는 컴파일 되면 사라짐

# SCSS 참고자료
