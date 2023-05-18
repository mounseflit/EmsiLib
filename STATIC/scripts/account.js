// Get the popup and close button elements
const popup = document.querySelector('.popup');
const closePopup = document.querySelector('.close-popup');

// Open the popup when the "Checkout" button is clicked
document.addEventListener('click', e => {
    if (e.target.classList.contains('checkout-button')) {
        popup.style.display = 'flex';
    }
});

// Close the popup when the "X" button or outside of the popup is clicked
popup.addEventListener('click', e => {
    if (e.target === popup || e.target === closePopup) {
        popup.style.display = 'none';
    }
});

// Show the edit profile form and hide the profile details
const editProfileButton = document.querySelector('.edit-profile-button');
const profileDetails = document.querySelector('.profile-details');
const editProfileForm = document.querySelector('.edit-profile-form');
const closeEditProfile = document.querySelector('.close-edit-profile');
const changeImageBtn = document.querySelector('.change-image-btn');
const popupOverlay = document.querySelector('.popup-overlay');
const popup1 = document.querySelector('.popup');


changeImageBtn.addEventListener('click', () => {
    popupOverlay.style.display = 'none';
    popup1.style.display = 'block';
});





editProfileButton.addEventListener('click', () => {
    profileDetails.style.display = 'none';
    editProfileForm.style.display = 'block';
});

closeEditProfile.addEventListener('click', () => {
    profileDetails.style.display = 'block';
    editProfileForm.style.display = 'none';
});

// Save updated user information when the form is submitted
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const addressInput = document.querySelector('#address');
const phoneInput = document.querySelector('#phone');

const nameOutput = document.querySelector('.user-name');
const emailOutput = document.querySelector('.profile-details li:nth-of-type(2)');
const addressOutput = document.querySelector('.profile-details li:nth-of-type(3)');
const phoneOutput = document.querySelector('.profile-details li:nth-of-type(4)');

const editProfileFormSubmit = document.querySelector('.edit-profile-form input[type="submit"]');

editProfileFormSubmit.addEventListener('click', e => {
    e.preventDefault();
    nameOutput.textContent = nameInput.value;
    emailOutput.textContent = `Email: ${emailInput.value}`;
    addressOutput.textContent = `Address: ${addressInput.value}`;
    phoneOutput.textContent = `Phone: ${phoneInput.value}`;

    profileDetails.style.display = 'block';
    editProfileForm.style.display = 'none';
});