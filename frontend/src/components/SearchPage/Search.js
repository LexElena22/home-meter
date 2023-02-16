import React from "react";
import axios from "axios";
import "./Search.css";
import Navbar from "../Navbar";
import { Button } from "../Button";

const API_HOST = "https://api.home-meter.com";

class Search extends React.Component {
  constructor(props) {
    super(props);

    this.mlsRef = React.createRef();
    this.mlsErrRef = React.createRef();
    this.findPropertyRef = React.createRef();
    this.checklistContainer = React.createRef();
    this.checklistRef = React.createRef();
    this.getResultsBtnRef = React.createRef();
    this.resultRef = React.createRef();
    this.resultPhotoRef = React.createRef();
    this.resultScoreRef = React.createRef();
    this.resultScoreImgRef = React.createRef();
    this.resultNameRef = React.createRef();
    this.resultDescriptionRef = React.createRef();
    this.resultPoiRef = React.createRef();
    this.resultCommunityRef = React.createRef();

    this.selectedCategories = 0;
  }

  //-------------Hide/Show-------------------

  hide = (domRef) => {
    domRef.current.className += " hidden";
  };
  show = (domRef) => {
    domRef.current.className = domRef.current.className.replace("hidden", "");
  };

  //-------------Checklist-------------------

  buildCheckListCategories = (categories) => {
    //  console.log(categories);
    this.show(this.checklistContainer);
    this.getResultsBtnRef.current.disabled = true;

    for (let i = 0; i < categories.length; i++) {
      this.checklistRef.current.appendChild(
        this.buildCategoryRow(categories[i], i)
      );
      let categoryItem = this.checklistRef.current.children[i];
      let checkbox = categoryItem.firstChild;
      checkbox.onchange = () => {
        let options = categoryItem.lastChild;
        if (options.className.includes("hidden")) {
          this.selectedCategories++;
          options.className = options.className.replace("hidden", "");
        } else {
          options.className += " hidden";
          this.selectedCategories--;
        }
        if (this.selectedCategories >= 5) {
          this.getResultsBtnRef.current.disabled = false;
        } else {
          this.getResultsBtnRef.current.disabled = true;
        }
      };
    }
  };
  //
  buildCategoryRow = (category, idx) => {
    var li = document.createElement("li");
    li.innerHTML =
      "<input type='checkbox' value='" +
      category +
      "'/><span class='category-name'>" +
      category +
      "</span>" +
      "<select class='priority-options hidden' id='cat-" +
      idx +
      "'><option value='1'>High</option><option value='2'>Medium</option><option value='3'>Low</option></select>";

    return li;
  };

  handleFindPropertyResponse = (categories) => {
    if (categories != null && categories.message != null) {
      this.mlsErrRef.current.innerText = categories.message;
    } else if (categories != null && categories.length > 0) {
      this.hide(this.findPropertyRef);
      this.buildCheckListCategories(categories);
    }
  };

  handleScoreResponse = (scoreData) => {
    // console.log(scoreData);

    this.hide(this.checklistContainer);
    this.show(this.resultRef);

    this.resultPhotoRef.current.src = scoreData.img;
    this.resultNameRef.current.innerHTML = scoreData.name;
    this.resultScoreRef.current.innerHTML = scoreData.score;
    this.resultScoreImgRef.current.src = scoreData.score_string + ".png";
    this.resultScoreImgRef.current.alt = scoreData.score_string;
    this.resultDescriptionRef.current.innerHTML = scoreData.description;

    if (scoreData.address) {
      this.show(this.resultPoiRef);
      this.show(this.resultCommunityRef);
      this.resultPoiRef.current.src =
        "https://poi.home-meter.com/poi.php?address=" + scoreData.address;
      this.resultCommunityRef.current.src =
        "https://poi.home-meter.com/community.php?zip=" + scoreData.zip;
    }
  };

  getSelectedCategoriesJson = () => {
    let result = {};
    let list = this.checklistRef.current.children;

    for (let i = 0; i < list.length; i++) {
      let listItem = list[i];
      let checkbox = listItem.firstChild;
      let selectOptions = listItem.lastChild;
      if (checkbox.checked) {
        let categoryName = checkbox.value;
        let priorityNumber = parseInt(selectOptions.value);
        result[categoryName] = priorityNumber;
      }
    }

    return result;
  };

  //------------- API Calls -------------------

  callFindPropertyApi = () => {
    let mls = this.mlsRef.current.value;
    axios
      .get(API_HOST + "/findproperty/" + mls)
      .then((result) => {
        if (result.data != null) this.handleFindPropertyResponse(result.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  callScorePropertyApi = () => {
    let mls = this.mlsRef.current.value;
    axios
      .post(API_HOST + "/score/" + mls, this.getSelectedCategoriesJson())
      .then((result) => {
        if (result.data != null) this.handleScoreResponse(result.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  render() {
    return (
      <>
        <Navbar />
        {/* ------Find Property------ */}
        <div ref={this.findPropertyRef} className="mls-container">
          <br />
          <h2>Let's find your home.</h2>
          <br />
          <br />
          <input
            ref={this.mlsRef}
            type="text"
            placeholder="mls id#"
            className="mls-input"
          />
          <span ref={this.mlsErrRef} className="mls-error" />
          <span />
          <br />
          <br />
          <br />
          <Button
            className="mls-submit-btn"
            onClick={this.callFindPropertyApi}
            buttonColor="primary"
          >
            Next
          </Button>
        </div>
        {/* ------Checklist------ */}
        <div
          ref={this.checklistContainer}
          className="hidden checklist-container"
        >
          <div className="checklist-intro">
            <h2 className="checklist-title">What's your top priorities?</h2>
            <br />
            <h4 className="checklist-subtitle">
              1. Pick at least 5 must-haves when it comes to your dream home.
            </h4>
            <h4 className="checklist-subtitle">
              2. Then rate your top picks with either lowest, mid, or highest
              priority.
            </h4>
            <br />
            <br />
          </div>
          <ul ref={this.checklistRef} className="checklist-items"></ul>
          <br />
          <br />
          <div className="checklist-submit-btn">
            <Button
              innerRef={this.getResultsBtnRef}
              onClick={this.callScorePropertyApi}
              buttonColor="primary"
              buttonSize="btn--medium"
            >
              Get Results
            </Button>
          </div>
        </div>
        {/* ------Results------ */}
        <div ref={this.resultRef} className="hidden">
          <div className="row">
            {/* Home Photo */}
            <img
              ref={this.resultPhotoRef}
              className="result-photo"
              src=""
              alt="home"
            />
            {/* Score */}
            <div className="result-score">
              <div className="result-score-top">
                <h3 className="result-score-text">Score: </h3>
                <strong ref={this.resultScoreRef} className="result-score-num">
                  ..
                </strong>
              </div>
              <img
                ref={this.resultScoreImgRef}
                src=""
                alt=""
                className="result-meter"
              ></img>
            </div>
          </div>
          {/* Summary */}
          <div className="result-summary">
            <p ref={this.resultNameRef} className="result-address">
              ..
            </p>
            <p ref={this.resultDescriptionRef} className="result-description">
              ..
            </p>
          </div>
          {/* Infographics */}
          {
            <iframe
              onload="scroll(0,0);"
              ref={this.resultPoiRef}
              title="poi"
              className="hidden poi-iframe"
            ></iframe>
          }
          {
            <iframe
              onload="scroll(0,0);"
              ref={this.resultCommunityRef}
              title="poi"
              className="hidden community-iframe"
            ></iframe>
          }
        </div>
      </>
    );
  }
}

export default Search;
