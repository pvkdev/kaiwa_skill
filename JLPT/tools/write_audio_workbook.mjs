import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const [input, output, previewPath] = process.argv.slice(2);
const { feed, rows } = JSON.parse(await fs.readFile(input, "utf8"));
const book = Workbook.create();
const sheet = book.worksheets.add("Audio RSS");
sheet.showGridLines = false;
sheet.tabColor = "#264D59";
const headers = ["Cấp · năm/tháng", "Tên file gốc", "Đối chiếu RSS", "URL audio (enclosure)", "Tên tập trên RSS", "Gói migration", "File nguồn trong JLPT"];
const last = Math.max(7 + rows.length, 8);
const body = sheet.getRange(`A1:G${last}`);
body.format.font.name = "Arial";
body.format.font.size = 10;
body.format.font.color = "#172C35";
body.format.verticalAlignment = "center";
for (const [i, width] of [152, 238, 201, 430, 232, 166, 320].entries()) {
  sheet.getCell(0, i).format.columnWidthPx = width;
}
sheet.getRange("A2").values = [["Audio đề JLPT"]];
sheet.getRange("A2").format.font.size = 16;
sheet.getRange("A2").format.font.bold = true;
sheet.getRange("A2").format.rowHeightPx = 29;
sheet.getRange("A4").values = [["RSS Spotify (HTTPS)"]];
sheet.getRange("A4").format.font.bold = true;
sheet.getRange("B4").values = [[feed || null]];
sheet.getRange("B4").format.fill = "#FFF1BB";
sheet.getRange("B4").format.rowHeightPx = 27;
sheet.getRange("B5").values = [["Dán link vào B4, lưu và đóng Excel, sau đó chạy tools/sync_exam_audio.ps1."]];
sheet.getRange("B5").format.font.italic = true;
sheet.getRange("A7:G7").values = [headers];
const headings = sheet.getRange("A7:G7").format;
headings.fill = "#264D59";
headings.font.bold = true;
headings.font.color = "#FFFFFF";
headings.horizontalAlignment = "center";
headings.rowHeightPx = 29;
if (rows.length) {
  const values = rows.map(row => row.map(value =>
    typeof value === "string" && value.startsWith("=") ? "'" + value : value));
  sheet.getRange(`A8:G${last}`).values = values;
  sheet.getRange(`A8:G${last}`).format.rowHeightPx = 23;
  for (let r = 9; r <= last; r += 2) sheet.getRange(`A${r}:G${r}`).format.fill = "#EEF4F5";
}
sheet.freezePanes.freezeRows(7);
book.recalculate();
const check = await book.inspect({ kind: "table", range: "Audio RSS!A7:G8", include: "values", tableMaxRows: 2, tableMaxCols: 7 });
if (!check.ndjson.includes("URL audio") || sheet.getRange("B4").values[0][0] !== (feed || null)) {
  throw new Error("Không đọc lại được phần nhập RSS hoặc tiêu đề workbook.");
}
if (rows.length && sheet.getCell(last - 1, 0).values[0][0] !== rows.at(-1)[0]) {
  throw new Error("Sai số dòng kiểm kê.");
}
if (previewPath) {
  const preview = await book.render({ sheetName: "Audio RSS", range: `A1:G${Math.min(last, 13)}`, scale: 0.85, format: "png" });
  await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(book)).save(output);
