function commonTemplate(item) {
   return "<option value='" + item.Value + "'>" + item.Text + "</option>";
 };
 function commonTemplate2(item) {
   return "<option value='" + item.Value + "'>***" + item.Text + "***</option>";
 };

 function commonMatch(selectedValue) {
   return this.When == selectedValue;
 };
