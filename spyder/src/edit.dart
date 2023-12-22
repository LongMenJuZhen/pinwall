import 'dart:io';

void main() async {
  var file = File('main.py');

  // 读取文件
  String contents = await file.readAsString();
  print('Before modification: $contents');

  // 修改文件内容
  contents = contents.replaceAll('122500', '123456');

  // 写入文件
  await file.writeAsString(contents);

  contents = await file.readAsString();
  print('After modification: $contents');
}
