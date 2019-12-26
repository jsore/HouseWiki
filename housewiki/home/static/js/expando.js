// ((e) => {

  const expandSection = (elm) => {
    // if (expando.hasAttribute)
    try {
      console.log(elm);
      let currentElm = document.getElementById(`${elm}`);

      //let currentElm = document.querySelector(elm)
      console.log(currentElm);
      document.getElementById(`${elm}`).classList.toggle("expanded");
        // currentElm.classList.toggle("expanded");
    } catch (e) {
      console.log(`script load error: ${e}`);
    }

  }


  const expandButtons = Array.from(document.querySelectorAll('.more-house-details'));
  let c = 0;
  let count = '';
  expandButtons.forEach((btn) => {
    // let c = 0;
    count = 'collapseBtn' + c;
    console.log('loaded');
    // btn.addEventListener('click', expandSection(this.window.document.));
    // let btns = document.getElementById('')

    let newBtn = document.createElement('button');
    newBtn.innerHTML = 'View more details';
    newBtn.addEventListener('click', expandSection(count));
    newBtn.setAttribute('id', count);

    document.querySelectorAll('.more-house-details-div')
      .insertAdjacentHTML('beforeend', `<button class="works">View more details</button>`);
    // btn.addEventListener('click', expandSection(count));

    // document.getElementById(`${count}`)
    c++;
    // btn.getElementById(btn)


  });

  const expandMe = Array.from(document.querySelectorAll('.expando-house-details'));

  expandMe.forEach(e => e.classList.remove("expanded"));


  // expandSection()
// })();
// const expandMe = document.getElementById(
//   'expando-house-details-id'
// );


// expandSection()



// let expandButton = document.getElementById("more-house-details-id");
// (() => {
  // document.getElementById("more-house-details-id")

// expandButtons.addEventListener("click", expandSection);
// expandMe.classList.toggle("expanded");


// expandSection()


// })();
