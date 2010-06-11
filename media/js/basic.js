// Set language
function setlang(language) {
	$('#setlang input[name=language]').val(language); //get the selected language
	$('#setlang').submit(); //submit to /i18n/setlang/
}