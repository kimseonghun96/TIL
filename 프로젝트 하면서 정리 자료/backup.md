```jsx
// 카테고리 별 관심사

HashInt.jsx

import "./HashInt.css";
import React, { useState } from "react";
import Hashadd from "../HashAdd/HashAdd";
import { useSelector, useDispatch } from "react-redux";
import { addCheckboxData } from "../../../../redux/reducers/checkData";

function HashInt({ showIntModal }) {
  //나중에 프롭스해서 데이터 가져올 거임
  const [intdata, setIntData] = useState([
  ]);

  //체크한 데이터 띄우기
  const [inputValue, setInputValue] = useState("");
  const [checkData, setCheckData] = useState([]);

  const addItem = () => {
    setCheckData([...checkData, inputValue]);
  };

  // for (let i = 0; i < intdata.length; i++) {
  //   console.log(intdata[i].clicked);
  // }
  // console.log(intdata);

  // const handleClick = (id) => {
  //   setIntData(
  //     intdata.map((item) =>
  //       item.id === id ? { ...item, clicked: !item.clicked } : item
  //     )
  //   );
  // };

  // 체크한 데이터 가져오기

  // const value = intdata.name;

  // const dispatch = useDispatch();
  // const checkedData = useSelector((state) => state.checkedData);

  const dispatch = useDispatch();
  const handleChange = (item) => {
    dispatch(addCheckboxData(item));
  };

  return (
    <div className="hashintdiv">
      <button
        className="category"
        onClick={() => {
          showIntModal();
        }}
      >
        스포츠
      </button>
      <div className="cainterestdiv">
        {intdata.map((item, idx) => {
          return (
            <div className="cainterestbox" key={item.id} data-idx={idx}>
              {/* <input
                type="checkbox"
                key={item.id}
                data-idx={idx}
                value={item.name}
                onChange={() => handleChange("item1")}
              /> */}
              <button
                className={`btn ${
                  item.clicked ? "changecaintBack" : "caintBack"
                }`}
                onClick={addItem}
                // onClick={() => {
                //   handleClick(item.id);
                // }}
                // key={item.id}
                // data-idx={idx}
                // value={item.name}
                // onChange={() => handleChange("item1")}
              >
                <input
                  type="checkbox"
                  key={item.id}
                  data-idx={idx}
                  value={item.name}
                  onChange={() => handleChange("item1")}
                />
                {item.name}

                {/* <input
                type="checkbox"
                checked={bChecked}
                key={item.id}
                data-idx={idx}
                onChange={(e) => checkHandler(e)}
              /> */}
                {/* <div>
                  {CheckData.map((data, index) => (
                    <div key={index}>{data}</div>
                  ))}
                </div> */}
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default HashInt;
```

```jsx
//0208
// 카테고리 별 관심사

import "../Hash.css";
import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { addCheckboxData } from "../../../../redux/reducers/checkData";
import HashAdd from "../HashComponent/HashAdd/HashAdd";

function HashInt({ showIntModal }) {
  //나중에 프롭스해서 데이터 가져올 거임
  const [intdata, setIntData] = useState([

  //체크한 데이터 띄우기 test
  const [inputValue, setInputValue] = useState([]);
  const [todoList, setTodoList] = useState([]);
  // 체크 박스가 체크된 상태인지 파악하기 위한 useState를 생성
  // const [isClicked, setIsClicked] = useState(false);
  // const handleClick = () => {
  //   setIsClicked(!isClicked);
  // };

  const handleClick = (id) => {
    setIntData(
      intdata.map((item) =>
        item.id === id ? { ...item, clicked: !item.clicked } : item
      )
    );
  };

  const addItem = (checked, id) => {
    if (checked) {
      setTodoList([...todoList, id]);
    } else {
      // 체크 해제
      setTodoList(todoList.filter((el) => el !== id));
    }
  };

  //체크박스의 onChange 이벤트 핸들러에서 action creator 함수를 호출하여 디스패치합니다.
  // const dispatch = useDispatch();
  // const [text, setText] = useState([]);
  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   dispatch(addCheckboxData(intdata.name));
  //   setText([]);
  // };

  return (
    <div className="hashintdiv">
      <HashAdd todoList={todoList} />
      <button
        className="category"
        onClick={() => {
          showIntModal();
        }}
      >
        스포츠
      </button>
      <div className="cainterestdiv">
        {intdata.map((item, idx) => {
          return (
            <div className="cainterestbox" key={item.id} data-idx={idx}>
              <button
                className={`btn ${
                  item.clicked ? "changecaintBack" : "caintBack"
                }`}
                onClick={() => {
                  handleClick(item.id);
                }}
              >
                <input
                  type="checkbox"
                  key={item.id}
                  data-idx={idx}
                  value={item.name}
                  // onClick={addItem}
                  // onChange={(event) => setInputValue(event.target.value)}
                  onChange={(e) => {
                    addItem(e.currentTarget.checked, item.name);
                  }}
                  // onChange={(e) => setText(e.target.value)}
                  checked={todoList.includes(item.name) ? true : false}
                />

                {item.name}
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default HashInt;
```

## 0208

```jsx
//카테고리 선택 창

import "./Hash.css";
import React, { useState, useEffect } from "react";
import HashInt from "./HashComponent/HashInt";
import dummy from "../../../db/data.json";

import HashAdd from "./HashComponent/HashAdd/HashAdd";
// import axios from "axios";
// axios.defaults.baseURL = "<http://192.168.31.73:8000>";

function Hash({ showHashModal, showAlertModal }) {
  //카테고리 창인데 이걸 프롭스해서 창의 관심사로 가야할 거 같은데?
  // const API_URL = "blur-profile/profile/dddd";

  // const getCategories = () => {
  //   axios({
  //     method: "get",
  //     url: `/getAllCategories`,
  //     data: {
  //       userId: "dddd",
  //     },
  //   })
  //     .then((res) => {
  //       console.log(res.data);
  //     })
  //     .catch((err) => {
  //       alert("카테고리 없다.");
  //       console.log(err);
  //     });
  // };

  // const categories = [
  //   { categoryName: "1" },
  //   { categoryName: "2" },
  //   { categoryName: "3" },
  //   { categoryName: "4" },
  //   { categoryName: "5" },
  //   { categoryName: "6" },
  //   { categoryName: "7" },
  //   { categoryName: "8" },
  //   { categoryName: "9" },
  //   { categoryName: "10" },
  //   { categoryName: "11" },
  //   { categoryName: "12" },
  //   { categoryName: "13" },
  //   { categoryName: "14" },
  //   { categoryName: "15" },
  //   { categoryName: "16" },

  // ];

  function Category({ category, todoList }) {
    return (
      <div className="intBack" onClick={showIntModal}>
        {category.name}
      </div>
    );
  }

  const [intModal, setIntModal] = useState(false);
  const showIntModal = () => {
    setIntModal((pre) => !pre);
  };

  // //  추가 데이터 저장
  // const [checkList, setCheckList] = useState([]);
  // const addIte = () => {
  //   console.log("im hererere!");
  // };

  // //검색기능
  const [data, setData] = useState([
    { id: 1, name: "축구", clicked: false },
    { id: 2, name: "농구", clicked: false },
    { id: 3, name: "아이스하키", clicked: false },
    { id: 4, name: "스쿼시", clicked: false },
    { id: 5, name: "아스날", clicked: false },
    { id: 6, name: "외데고르", clicked: false },
    { id: 7, name: "파티", clicked: false },
    { id: 8, name: "마르치넬리", clicked: false },
    { id: 9, name: "은케티아", clicked: false },
    { id: 10, name: "램즈데일", clicked: false },
    { id: 11, name: "살리바", clicked: false },
    { id: 12, name: "마갈량이스", clicked: false },
    { id: 13, name: "사카", clicked: false },
    { id: 14, name: "자카", clicked: false },
    { id: 15, name: "진첸코", clicked: false },
    { id: 16, name: "이단아", clicked: false },
    { id: 17, name: "빡대가리", clicked: false },
    { id: 18, name: "라서", clicked: false },
    { id: 19, name: "힘이", clicked: false },
    { id: 20, name: "든다", clicked: false },
  ]);

  const [searchTerm, setSearchTerm] = useState("");
  const [results, setResults] = useState([]);

  //  그냥 서치바 초기에 안보이게 설정해야됨
  const [searchBar, setSearchBar] = useState(false);
  const showSearchBar = () => {
    setSearchBar((pre) => !pre);
  };

  useEffect(() => {
    const results = data.filter((item) =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setResults(results);
  }, [searchTerm]);

  //search 바
  function HashSerch() {
    return (
      <div>
        <div className="hashSerchbar">
          {results.map((item) => (
            <div className="ilserchbar" key={item.name}>
              {item.name}
            </div>
          ))}
        </div>
      </div>
    );
  }

  // TEST
  const [inputValue, setInputValue] = useState("");
  const [todoList, setTodoList] = useState([]);

  const addItem = () => {
    setTodoList([...todoList, inputValue]);
  };

  //////////////////////////////////////////
  return (
    <div className="Hash">
      {/* <button onClick={getCategories}>dddd</button> */}

      {intModal ? <HashInt showIntModal={setIntModal} /> : null}
      {searchBar ? <HashSerch showSearchBar={setSearchBar} /> : null}

      {/* <HashAdd todoList={todoList} />
      <input
        value={inputValue}
        type="text"
        onChange={(event) => setInputValue(event.target.value)}
      />
      <button onClick={addItem}>추가</button> */}

      <div className="hashSerchDiv">
        <div className="inputdodbogi" />
        <input
          className="hashinput"
          type="text"
          value={searchTerm}
          placeholder="관심사를 찾아보세요."
          onChange={(e) => setSearchTerm(e.target.value)}
          onClick={showSearchBar}
        />

        <div className="hashVec" />
      </div>

      {/* <div className="interestdiv">
        {categories.map((category, idx) => {
          return (
            <div className="interestbox">

              <Category key={category.id} category={category} />
            </div>
          );
        })}
      </div> */}

      <button
        className="hashEdit"
        onClick={() => {
          showHashModal();
          showAlertModal();
        }}
      >
        선호 정보 수정
      </button>
    </div>
  );
}

export default Hash;
```

```jsx
// 카테고리 별 관심사

import "../Hash.css";
import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { addCheckboxData } from "../../../../redux/reducers/checkData";
import HashAdd from "./HashAdd";
import Hash from "../Hash";
import axios from "axios";

function HashInt({ showIntModal, Category }) {
  // function Category({ category, todoList }) {
  //   return (
  //     <div className="intBack" onClick={showIntModal}>
  //       {category.name}
  //     </div>
  //   );
  // }
  const getCategories = () => {
    axios({
      method: "GET",
      url: `http://192.168.31.73:8000/blur-profile/profile/dddd/getAllInterests`,
      data: {},
    })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        alert("카테고리 없다.");
        console.log(err);
      });
  };

  //나중에 프롭스해서 데이터 가져올 거임
  // const [intdata, setIntData] = useState([
  //   { name: "축구" },
  //   { name: "농구" },
  //   { name: "아이스하키" },
  //   { name: "스쿼시" },
  //   { name: "아스날" },
  //   { name: "외데고르" },
  //   { name: "파티" },
  //   { name: "최동호" },
  //   { name: "김창겸" },
  //   { name: "박주승" },
  //   { name: "송대현" },

  //   { name: "김원웅" },
  //   { name: "강정훈" },
  //   { name: "1" },
  //   { name: "2" },
  //   { name: "3" },
  //   { name: "4" },
  //   { name: "5" },
  //   { name: "6" },
  //   { name: "7" },
  //   { name: "8" },
  //   { name: "9" },

  //   { name: "10" },
  //   { name: "11" },
  //   { name: "12" },
  //   { name: "13" },
  //   { name: "14" },
  //   { name: "15" },
  // ]);

  // console.log({ Category });

  //체크한 데이터 띄우기 test
  const [inputValue, setInputValue] = useState([]);
  const [todoList, setTodoList] = useState([]);

  // 개별요소 색상 변경하기 위한 코드
  const handleClick = (name) => {
    setIntData(
      intdata.map((item) =>
        item.name === name ? { ...item, clicked: !item.clicked } : item
      )
    );
  };

  // 체크 데이터 추가할 거
  const addItem = (checked, name) => {
    if (checked) {
      setTodoList([...todoList, name]);
    } else {
      // 체크 해제
      setTodoList(todoList.filter((el) => el !== name));
    }
  };

  return (
    <div className="hashintdiv">
      <HashAdd todoList={todoList} />
      <div className="cainterestdiv">
        {intdata.map((item, idx) => {
          return (
            <div className="cainterestbox" key={item.name} data-idx={idx}>
              <button
                className={`btn ${
                  item.clicked ? "changecaintBack" : "caintBack"
                }`}
                onClick={() => {
                  handleClick(item.name);
                }}
              >
                <input
                  type="checkbox"
                  key={item.name}
                  data-idx={idx}
                  value={item.name}
                  onChange={(e) => {
                    addItem(e.currentTarget.checked, item.name);
                  }}
                  checked={todoList.includes(item.name) ? true : false}
                />

                {item.name}
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default HashInt;
```

```jsx
// 백엔드 통신 방법

// 버튼으로 확인 하는 법
const getProfile = () => {
    axios({
      method: "GET",
      url: `${API_URL}/${id}`,
      data: {},
    })
      .then((res) => {
        console.log(res.data);
        console.log(res.status);
      })
      .catch((err) => {
        alert("기존 데이터 없다");
        console.log(err);
      });
  };

// 화면 켜지자 말자 띄우는 거
  const [proFile, setProFile] = useState([]);
  useEffect(() => {
    axios({
      method: "GET",
      url: `${API_URL}/${id}`,
      data: {},
    })
      .then((res) => {
        console.log(res.data);
        console.log(res.status);
        setProFile(res.data);
        console.log("성공><");
      })
      .catch((err) => {
        alert("기존 데이터 없다.");
        console.log(err);
      });
  }, []);

const handleSave = async () => {
    console.log(nameInput);
    console.log(ageInput);
    console.log(introInput);
    const response = await fetch(`${API_URL}/${id}/updateProfile`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userId: id,
        age: ageInput,
        nickname: nameInput,
        // image: document.querySelector(".leftModalImg"),
        // gender: gender,
        introduce: introInput,
        // mbti: mbti,
      }),
    });
    if (response.ok) {
      console.log("성공적으로 업데이트 됐다.");
    } else {
      console.error("실패했다.");
    }
  };
```

```jsx
// 로딩 스피너       <div className="squish-unsquish"></div>
.squish-unsquish {
  position: relative;
  width: 10em;
  height: 10em;
  background-image: url(../../../public/heartIcon.ico);
  background-size: 100% 100%;
  border-radius: 20%;
  animation: squish-unsquish 0.5s ease-in-out infinite alternate;
}

@keyframes squish-unsquish {
  0% {
    transform: scale(0.8, 0.8);
  }
  50% {
    transform: scale(0.7, 0.7);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

```jsx
<div className="cainterestdiv">
    {intdata.map((item, idx) => {
      const selected = checkData.includes(item.interestName);
      return (
        <div
          className="cainterestbox"
          key={item.interestName}
          data-idx={idx}
        >
          <button
            className={`btn ${selected ? "changecaintBack" : "caintBack"}`}
            onClick={() => {
              handleClick(item.interestName);
            }}
          >
            <input
              className="custom-checkbox-style"
              type="checkbox"
              key={item.interestName}
              data-idx={idx}
              value={item.interestName}
              checked={selected}
              onChange={(e) => {
                handleClickk(item.interestName);
              }}
            />
        {item.interestName}
      </button>
    </div>
  );
  })}

  </div>
```

```
// 카테고리 별 관심사

import "../Hash.css";
import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import Checkdata from "./Checkdata";

function HashInt({}) {
  // useEffect 함수를 사용하여 데이터를 가져오는 방법
  // const [intdata, setIntData] = useState([]);

  // useEffect(() => {
  //   axios({
  //     method: "GET",
  //     url: `http://192.168.31.73:8000/blur-profile/profile/dddd/getAllInterests`,
  //     data: {},
  //   })
  //     .then((res) => {
  //       console.log(res.data.interests);
  //       console.log(res.status);
  //       setIntData(res.data.interests);
  //     })
  //     .catch((err) => {
  //       alert("카테고리 없다.");
  //       console.log(err);
  //     });
  // }, []);

    const [intdata, setIntData] = useState([
      {interestName : '이단아'},
      {interestName : '김성훈'},
      {interestName : '김은재'},

      {interestName : '박유정'},

      {interestName : '박현수'},
      {interestName : '조인애'},

      { interestName : '이한아'},
      {interestName : '이현아'},

    ]);

  const [checkData, setcheckData] = useState([]);   //체크한 데이터 띄우기 

  const [limit, setLimit] = useState(5);

  const handleRemove = (item) => {
    setcheckData((prev) => prev.filter((intdata) => intdata !== item));
  };

  const handleClick = (interestName) => {
    if (checkData.length >= limit) {
      // alert(`최대 ${limit}개만 선택 가능합니다.`);
      return;
    }
    const found = checkData.find((data) => data === interestName);
    if (found) {
      handleRemove(interestName);
    } else {
      setcheckData((prev) => [...prev, interestName]);
    }
  };


  console.log("HashInt", checkData)

  return (
    <div className="hashintdiv">
      <div>
        <div className="hashaddiv">
          {checkData && checkData.map((item) => (
            <Checkdata item={item} onRemove={() => handleRemove(item)} />
          ))}
        </div>
      </div>
      <div className="cainterestdiv">
        {intdata.map((item, idx) => {
          const selected = checkData.includes(item.interestName);
          return (
            <div
              className="cainterestbox"
              key={item.interestName}
              data-idx={idx}
            >
              <button
                className={`btn ${selected ? "changecaintBack" : "caintBack"}`}
              >
                <input
                  className="custom-checkbox-style"
                  type="checkbox"
                  key={item.interestName}
                  data-idx={idx}
                  value={item.interestName}
                  checked={selected}
                  onChange={(e) => {
                    handleClick(item.interestName);
                  }}
                />
                {item.interestName}
              </button>
            </div>
          );
        })}
      </div>
  </div>
  );
}

export default HashInt;
    {/* <div className="cainterestdiv">
        {intdata.map((item, idx) => {
          const selected = checkData.includes(item.interestName)
          return (
            <div
              className="cainterestbox"
              key={item.interestName}
              data-idx={idx}
            >
              <button
                className={`btn ${selected ? "changecaintBack" : "caintBack"}`}
                onClick={() => {
                  handleClick(item.interestName);
                }}
              >
                <input
                  className="custom-checkbox-style"
                  type="checkbox"
                  key={item.interestName}
                  data-idx={idx}
                  value={item.interestName}
                  onChange={(e) => {
                    addItem(e.currentTarget.checked, item.interestName);
                  }}
                />

                {item.interestName}
              </button>
            </div>
          );
        })}
      </div> */}
```

```jsx
//카테고리 선택 창

import "./Hash.css";
import React, { useState, useEffect, useRef } from "react";
import HashInt from "./HashComponent/HashInt";
import HashSerch from "./HashComponent/HashSerch";
import InterestList from "./HashComponent/InterestList";
// import HashAdd from "./HashComponent/HashAdd/HashAdd";
import axios from "axios";

function Hash({ showHashModal, showAlertModal }) {
  // const API_URL = "blur-profile/profile/dddd";

  const getCategories = () => {
    axios({
      method: "GET",
      url: `http://192.168.31.73:8000/blur-profile/profile/dddd/getAllInterests`,
      data: {},
    })
      .then((res) => {
        console.log(res.data);
        console.log(res.status);
      })
      .catch((err) => {
        alert("카테고리 없다.");
        console.log(err);
      });
  };

  // 관심사 모달 띄우는 거
  const [intModal, setIntModal] = useState(false);
  const showIntModal = () => {
    setIntModal((pre) => !pre);
  };
  // //검색기능 데이터

  // props 해서 데이터 좀 옮겨 주세요
  const [intdata, setIntData] = useState([
    { interestName: "이단아" },
    { interestName: "김성훈" },
    { interestName: "김은재" },

    { interestName: "박유정" },

    { interestName: "박현수" },
    { interestName: "조인애" },

    { interestName: "이한아" },
    { interestName: "이현아" },
  ]);

  const [searchTerm, setSearchTerm] = useState("");
  const [results, setResults] = useState([]);

  useEffect(() => {
    const results = intdata.filter((item) =>
      item.interestName.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setResults(results);
  }, [searchTerm]);

  //  그냥 서치바 초기에 안보이게 설정해야됨
  const [searchBar, setSearchBar] = useState(false);
  const showSearchBar = () => {
    setSearchBar((pre) => !pre);
  };

  //search 바
  // function HashSerch() {
  //   return (
  //     <div>
  //       <div className="hashSerchbar">
  //         {results.map((item) => (
  //           <div className="ilserchbar">{item.interestName}</div>
  //         ))}
  //       </div>
  //     </div>
  //   );
  // }

  // TEST 데이터 띄우기
  const [inputValue, setInputValue] = useState("");
  const [checkData, setcheckData] = useState([]);

  const addItem = () => {
    setcheckData([...checkData, inputValue]);
  };

  // // 검색 test
  // const [searchTerm, setSearchTerm] = useState("");

  // const handleSearch = (event) => {
  //   setSearchTerm(event.target.value);
  // };

  // const filteredIntData = intdata.filter((item) => {
  //   return item.interestName.includes(searchTerm);
  // });

  //////////////////////////////////////////

  const HashSerch = ({ results, handleClick }) => {
    const handleClickOutside = (event) => {
      if (ref.current && !ref.current.contains(event.target)) {
        handleClick();
      }
    };

    const ref = useRef();
    useEffect(() => {
      document.addEventListener("click", handleClickOutside);
      return () => {
        document.removeEventListener("click", handleClickOutside);
      };
    });

    return (
      <div ref={ref}>
        <div className="hashSerchbar">
          {results.map((item) => (
            <div className="ilserchbar">{item.interestName}</div>
          ))}
        </div>
      </div>
    );
  };
  const [suggestions, setSuggestions] = useState([]);
  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
    setSuggestions(intdata.filter((item) => item.interestName.includes(searchTerm)));
    };

    const handleSuggestionClick = (suggestion) => {
    setSearchTerm(suggestion);
    setSuggestions([]);
    };

    const filteredIntData = intdata.filter((item) => {
    return item.interestName.includes(searchTerm);
    });
  return (
    <div className="Hash">
      <HashInt intdata={intdata} />
      {/* <HashInt getCategories={getCategories} /> */}
      {/* <button onClick={getCategories}>ddd</button> */}
      {intModal ? <HashInt showIntModal={setIntModal} /> : null}
      {searchBar ? <HashSerch showSearchBar={setSearchBar} /> : null}

      <div className="hashSerchDiv">
        <div className="inputdodbogi" />
        <input
className="hashinput"
      type="text"
    placeholder="관심사를 찾아보세요."
      value={searchTerm}
      onChange={handleSearch}
    />
    {searchTerm !== "" && (
      <HashSerch results={filteredIntData} handleClick={() => setSearchTerm("")} />
    )}


        <div className="hashVec" />
      </div>

      <HashInt />

      <button
        className="hashEdit"
        onClick={() => {
          showHashModal();
          showAlertModal();
        }}
      >
        선호 정보 수정
      </button>
    </div>
  );
}

export default Hash;
```

```jsx
//카테고리 선택 창

import "./Hash.css";
import React, { useState, useEffect, useRef } from "react";
import HashInt from "./HashComponent/HashInt";
import HashSerch from "./HashComponent/HashSerch";
import InterestList from "./HashComponent/InterestList";
// import HashAdd from "./HashComponent/HashAdd/HashAdd";
import axios from "axios";

function Hash({ showHashModal, showAlertModal }) {
  // const API_URL = "blur-profile/profile/dddd";

  const getCategories = () => {
    axios({
      method: "GET",
      url: `http://192.168.31.73:8000/blur-profile/profile/dddd/getAllInterests`,
      data: {},
    })
      .then((res) => {
        console.log(res.data);
        console.log(res.status);
      })
      .catch((err) => {
        alert("카테고리 없다.");
        console.log(err);
      });
  };

  // 관심사 모달 띄우는 거
  const [intModal, setIntModal] = useState(false);
  const showIntModal = () => {
    setIntModal((pre) => !pre);
  };
  // //검색기능 데이터

  // props 해서 데이터 좀 옮겨 주세요
  const [intdata, setIntData] = useState([
    { interestName: "이단아" },
    { interestName: "김성훈" },
    { interestName: "김은재" },

    { interestName: "박유정" },

    { interestName: "박현수" },
    { interestName: "조인애" },

    { interestName: "이한아" },
    { interestName: "이현아" },
  ]);

  const [searchTerm, setSearchTerm] = useState("");
  const [results, setResults] = useState([]);

  useEffect(() => {
    const results = intdata.filter((item) =>
      item.interestName.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setResults(results);
  }, [searchTerm]);

  //  그냥 서치바 초기에 안보이게 설정해야됨
  const [searchBar, setSearchBar] = useState(false);
  const showSearchBar = () => {
    setSearchBar((pre) => !pre);
  };

  //search 바
  // function HashSerch() {
  //   return (
  //     <div>
  //       <div className="hashSerchbar">
  //         {results.map((item) => (
  //           <div className="ilserchbar">{item.interestName}</div>
  //         ))}
  //       </div>
  //     </div>
  //   );
  // }

  // TEST 데이터 띄우기
  const [inputValue, setInputValue] = useState("");
  const [checkData, setcheckData] = useState([]);

  const addItem = () => {
    setcheckData([...checkData, inputValue]);
  };

  // // 검색 test
  // const [searchTerm, setSearchTerm] = useState("");

  // const handleSearch = (event) => {
  //   setSearchTerm(event.target.value);
  // };

  // const filteredIntData = intdata.filter((item) => {
  //   return item.interestName.includes(searchTerm);
  // });

  //////////////////////////////////////////

  const HashSerch = ({ results, handleClick }) => {
    const handleClickOutside = (event) => {
      if (ref.current && !ref.current.contains(event.target)) {
        handleClick();
      }
    };

    const ref = useRef();
    useEffect(() => {
      document.addEventListener("click", handleClickOutside);
      return () => {
        document.removeEventListener("click", handleClickOutside);
      };
    });

    return (
      <div ref={ref}>
        <div className="hashSerchbar">
          {results.map((item) => (
            <div className="ilserchbar">{item.interestName}</div>
          ))}
        </div>
      </div>
    );
  };
  return (
    <div className="Hash">
      <HashInt intdata={intdata} />
      {/* <HashInt getCategories={getCategories} /> */}
      {/* <button onClick={getCategories}>ddd</button> */}
      {intModal ? <HashInt showIntModal={setIntModal} /> : null}
      {searchBar ? <HashSerch showSearchBar={setSearchBar} /> : null}

      <div className="hashSerchDiv">
        <div className="inputdodbogi" />
        <input
          className="hashinput"
          type="text"
          value={searchTerm}
          placeholder="관심사를 찾아보세요."
          onChange={(e) => setSearchTerm(e.target.value)}
          onClick={showSearchBar}
        />


        <div className="hashVec" />
      </div>

      <HashInt />

      <button
        className="hashEdit"
        onClick={() => {
          showHashModal();
          showAlertModal();
        }}
      >
        선호 정보 수정
      </button>
    </div>
  );
}

export default Hash;
```
