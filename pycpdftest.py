import pycpdf
import sys
import os

if sys.platform.startswith('darwin'):
  pycpdf.loadDLL("/Users/john/repos/python-libcpdf/libpycpdf.so")
elif sys.platform.startswith('linux'):
  pycpdf.loadDLL("libpycpdf.so")
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    os.add_dll_directory("C:\\\\OCaml64/home/JohnWhitington/python-libcpdf/")
    pycpdf.loadDLL("libpycpdf.dll")

def prerr():
  print("*** EXCEPTION RAISED")
  print(f'({pycpdf.lastError()} | {pycpdf.lastErrorString()})')
  pycpdf.clearError()

#CHAPTER 0. Preliminaries
print('***** CHAPTER 0. Preliminaries')
print('---cpdf_startup()')
try: pycpdf.startup()
except: prerr()
print('---cpdf_version()')
try: print('version = ' + pycpdf.version())
except: prerr()
print('---cpdf_setFast()')
try: pycpdf.setFast()
except: prerr()
print('---cpdf_setSlow()')
try: pycpdf.setSlow()
except: prerr()
print('---cpdf_clearError()')
try: pycpdf.clearError()
except: prerr()
print('---cpdf_onExit()')
try: pycpdf.onExit()
except: prerr()

#CHAPTER 1. Basics
print('***** CHAPTER 1. Basics')
print('---cpdf_fromFile()')
pdf = pycpdf.fromFile('cpdflibmanual.pdf', '')
prerr()
print('---cpdf_fromFileLazy')
pdf2 = pycpdf.fromFileLazy('testinputs/cpdfmanual.pdf', '')
prerr()
fh = open('testinputs/cpdfmanual.pdf', mode='rb')
data = fh.read()
print('---cpdf_fromMemory')
pdf3 = pycpdf.fromMemory(data, '')
prerr()
print('---cpdf_fromMemoryLazy')
pdf4 = pycpdf.fromMemoryLazy(data, '')
prerr()
print('---cpdf_blankDocument')
pdf5 = pycpdf.blankDocument(200.5, 100.0, 50)
prerr()
print('---cpdf_toFile')
pycpdf.toFile(pdf5, 'testoutputs/blank.pdf', False, False)
prerr()
print('---cpdf_blankDocumentPaper')
pdf6 = pycpdf.blankDocumentPaper(pycpdf.a3landscape, 50)
prerr()
pycpdf.toFile(pdf6, 'testoutputs/blank2.pdf', False, False)
print('---cpdf_enumeratePDFs')
pdfs = pycpdf.enumeratePDFs()
prerr()
for k, i in pdfs:
  print(k, i)
print('---cpdf_ptOfCm')
print(pycpdf.ptOfCm(1.0))
prerr()
print('---cpdf_ptOfMm')
print(pycpdf.ptOfMm(1.0))
prerr()
print('---cpdf_ptOfIn')
print(pycpdf.ptOfIn(1.0))
prerr()
print('---cpdf_cmOfPt')
print(pycpdf.cmOfPt(1.0))
prerr()
print('---cpdf_ptOfCm')
print(pycpdf.mmOfPt(1.0))
prerr()
print('---cpdf_ptOfCm')
print(pycpdf.inOfPt(1.0))
prerr()
print('---cpdf_parsePagespec')
r = pycpdf.parsePagespec(pdf4, "1-3,end")
prerr()
print('---cpdf_valiadatePagespec')
valid = pycpdf.validatePagespec("1-4,5,6")
prerr()
print('---cpdf_all')
allpdf4 = pycpdf.all(pdf4)
prerr()
print(allpdf4)
print('---cpdf_stringOfPagespec')
pagespecstr = pycpdf.stringOfPagespec(pdf4, allpdf4)
prerr()
print(pagespecstr)
print('---cpdf_blankRange')
blankrange = pycpdf.blankRange()
prerr()
print('---cpdf_pageRange')
fromto = pycpdf.pageRange(3, 7)
print('---cpdf_all')
rall = pycpdf.all(pdf4)
prerr()
print("all", rall)
print('---cpdf_even')
even = pycpdf.even(rall)
prerr()
print('---cpdf_odd')
odd = pycpdf.odd(rall)
prerr()
print('---cpdf_rangeUnion')
union = pycpdf.rangeUnion(even, odd)
prerr()
print('---cpdf_difference')
difference = pycpdf.difference(even, odd)
prerr()
print('---cpdf_removeDuplicates')
nodeps = pycpdf.removeDuplicates(rall)
prerr()
print('---cpdf_rangeLength')
rangel = pycpdf.rangeLength(union)
prerr()
print('---cpdf_rangeGet')
got = pycpdf.rangeGet(odd, 1)
prerr()
print('---cpdf_rangeAdd')
added = pycpdf.rangeAdd(odd, 9)
prerr()
print('---cpdf_isInRange')
inrange = pycpdf.isInRange(odd, 1)
prerr()
print('---cpdf_pages')
pages = pycpdf.pages(pdf5)
prerr()
print('---cpdf_pagesFast')
pagesf = pycpdf.pagesFast('', 'testinputs/cpdfmanual.pdf')
prerr()
print('---cpdf_toFile')
pycpdf.toFile(pdf4, 'testoutputs/toFile.pdf', False, False)
prerr()
print('---cpdf_toFileExt')
pycpdf.toFileExt(pdf4, 'testoutputs/toFileExt.pdf', False, False, False, False, False)
prerr()
print('---cpdf_toMemory')
tomembytes = pycpdf.toMemory(pdf5, False, False)
prerr()
print('---cpdf_isEncrypted')
isenc = pycpdf.isEncrypted(pdf5)
prerr()
print('---cpdf_toFileEncrypted')
pycpdf.toFileEncrypted(pdf5, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, 'testoutputs/enc.pdf')
prerr()
print('---cpdf_toFileEncryptedExt')
pycpdf.toFileEncryptedExt(pdf5, pycpdf.pdf40bit, [pycpdf.noEdit], 'owner', 'user', False, False, False, False, False, 'testoutputs/enc2.pdf')
prerr()
encpdf = pycpdf.fromFile('testoutputs/enc.pdf', 'user')
print('---cpdf_decryptPdf')
decrypted = pycpdf.decryptPdf(encpdf, 'user')
prerr()
encpdf2 = pycpdf.fromFile('testoutputs/enc.pdf', 'user')
print('---cpdf_decryptPdfOwner')
owner = pycpdf.decryptPdfOwner(encpdf2, 'owner')
prerr()
print('---cpdf_hasPermission')
hasperm = pycpdf.hasPermission(encpdf2, pycpdf.noEdit)
prerr()
print('---cpdf_encryptionKind')
encmethod = pycpdf.encryptionKind(encpdf2)
prerr()

# CHAPTER 2. Merging and Splitting
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
pdf2 = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print('---cpdf_mergeSimple')
print(pdf, pdf2)
merged = pycpdf.mergeSimple([pdf, pdf2])
prerr()
pycpdf.toFile(merged, 'testoutputs/merged.pdf', False, False)
print('---cpdf_merge')
merged2 = pycpdf.merge([pdf, pdf2], True, False)
prerr()
pycpdf.toFile(merged2, 'testoutputs/merged2.pdf', False, False)
print('---cpdf_mergeSame')
same = pycpdf.mergeSame([pdf, pdf2, pdf], True, False, [pycpdf.even(pycpdf.all(pdf)), pycpdf.all(pdf2), pycpdf.odd(pycpdf.all(pdf))])
prerr()
pycpdf.toFile(same, 'testoutputs/same.pdf', False, False)
print('---cpdf_selectPages')
selected = pycpdf.selectPages(pdf, pycpdf.even(pycpdf.all(pdf)))
prerr()
pycpdf.toFile(selected, 'testoutputs/selected.pdf', False, False)

# CHAPTER 3. Pages
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
r = pycpdf.all(pdf)
print('---cpdf_scalePages')
pycpdf.scalePages(pdf, r, 0.5, 0.7)
prerr()
print('---cpdf_scaleToFit')
pycpdf.scaleToFit(pdf, r, 0.5, 0.7, 0.5)
prerr()
print('---cpdf_scaleToFitPaper')
pycpdf.scaleToFitPaper(pdf, r, pycpdf.a3landscape, 0.5)
prerr()
print('---cpdf_scaleContents')
pycpdf.scaleContents(pdf, r, (pycpdf.top, 10, 10), 1.0)
prerr()
print('---cpdf_shiftContents')
pycpdf.shiftContents(pdf, r, 100, -100)
prerr()
print('---cpdf_rotate')
pycpdf.rotate(pdf, r, 90)
prerr()
print('---cpdf_rotateBy')
pycpdf.rotateBy(pdf, r, 180)
prerr()
print('---cpdf_rotateContents')
pycpdf.rotateContents(pdf, r, 43.3)
prerr()
print('---cpdf_upright')
pycpdf.upright(pdf, r)
prerr()
print('---cpdf_hFlip')
pycpdf.hFlip(pdf, r)
prerr()
print('---cpdf_vFlip')
pycpdf.vFlip(pdf, r)
prerr()
print('---cpdf_crop')
pycpdf.crop(pdf, r, 100.0, 100.0, 400.0, 400.0)
prerr()
print('---cpdf_removeCrop')
pycpdf.removeCrop(pdf, r)
prerr()
print('---cpdf_removeTrim')
pycpdf.removeTrim(pdf, r)
prerr()
print('---cpdf_removeArt')
pycpdf.removeArt(pdf, r)
prerr()
print('---cpdf_removeBleed')
pycpdf.removeBleed(pdf, r)
prerr()
print('---cpdf_trimMarks')
pycpdf.trimMarks(pdf, r)
prerr()
print('---cpdf_showBoxes')
pycpdf.showBoxes(pdf, r)
prerr()
print('---cpdf_hardBox')
pycpdf.hardBox(pdf, r, "/MediaBox")
prerr()

# CHAPTER 4. Encryption

# Encryption covered under Chapter 1 in cpdflib

# CHAPTER 5. Compression
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print('---cpdf_compress')
pycpdf.compress(pdf)
prerr()
print('---cpdf_decompress')
pycpdf.decompress(pdf)
prerr()
print('---cpdf_squeezeInMemory')
pycpdf.squeezeInMemory(pdf)
prerr()
pycpdf.toFile(pdf, 'testoutputs/squeezed.pdf', False, False)

# CHAPTER 6. Bookmarks

# Format: list of tuples. (level : int, page : int, text : string, openstatus : int/bool) 
print('---cpdf_getBookmarks')
existing_marks = pycpdf.getBookmarks(pdf)
prerr()
print(existing_marks)
marks = [(0, 1, "new bookmark", True), (1, 3, "second, indented one", False)]
print('---cpdf_setBookmarks')
pycpdf.setBookmarks(pdf, marks)
prerr()

# CHAPTER 7. Presentations

# Not included in the library version

# CHAPTER 8. Logos, Watermarks and Stamps
print('---cpdf_stampOn')
pycpdf.stampOn(pdf, pdf2, r)
prerr()
print('---cpdf_stampUnder')
pycpdf.stampUnder(pdf, pdf2, r)
prerr()
print('---cpdf_stampExtended')
pycpdf.stampExtended(pdf, pdf2, r, True, True, pycpdf.topLeft, False)
prerr()
print('---cpdf_combinePages')
pycpdf.combinePages(pdf, pdf2)
prerr()
print('---cpdf_addText')
pycpdf.addText(False, pdf, r, 'The text', (pycpdf.topLeft, 1.0, 0.0), 1.0, 10, pycpdf.timesRoman, 12, 0.5, 0.5, 0.5, False, False, False, 1.0, pycpdf.centreJustify, True, False, 'foo.pdf', 2.0, False)
prerr()
print('---cpdf_addTextSimple')
pycpdf.addTextSimple(pdf, r, 'The text', (pycpdf.posCentre, 100.0, 200.0), pycpdf.timesRoman, 12.0)
prerr()
print('---cpdf_removeText')
pycpdf.removeText(pdf, r)
prerr()
print('---cpdf_textWidth')
pycpdf.textWidth(pycpdf.timesRoman, 'Some text')
prerr()

# CHAPTER 9. Multipage facilities
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print('---cpdf_twoUp')
pycpdf.twoUp(pdf)
prerr()
print('---cpdf_twoUpStack')
pycpdf.twoUpStack(pdf)
prerr()
r = pycpdf.all(pdf)
print('---cpdf_padBefore')
pycpdf.padBefore(pdf, r)
prerr()
print('---cpdf_padAfter')
pycpdf.padAfter(pdf, r)
prerr()
print('---cpdf_padEvery')
pycpdf.padEvery(pdf, 10)
prerr()
print('---cpdf_padMultiple')
pycpdf.padMultiple(pdf, 10)
prerr()
print('---cpdf_padMultipleBefore')
pycpdf.padMultipleBefore(pdf, 10)
prerr()
pycpdf.toFile(pdf, 'testoutputs/squeezed.pdf', False, False)

# CHAPTER 10. Annotations

# Not in the library version.

# CHAPTER 11. Document Information and Metadata
print('---cpdf_isLinearized')
linearized = pycpdf.isLinearized('testinputs/cpdfmanual.pdf')
prerr()
print('---cpdf_getVersion')
version = pycpdf.getVersion(pdf)
prerr()
print('---cpdf_getMajorVersion')
version2 = pycpdf.getMajorVersion(pdf)
prerr()
print('---cpdf_getTitle')
title = pycpdf.getTitle(pdf)
prerr()
print(f'title: {title}')
print('---cpdf_getTitle')
author = pycpdf.getAuthor(pdf)
prerr()
print(f'author: {author}')
print('---cpdf_getSubject')
subject = pycpdf.getSubject(pdf)
prerr()
print(f'subject: {subject}')
print('---cpdf_getKeywords')
keywords = pycpdf.getKeywords(pdf)
prerr()
print(f'keywords: {keywords}')
print('---cpdf_getCreator')
creator = pycpdf.getCreator(pdf)
prerr()
print(f'creator: {creator}')
print('---cpdf_getProducer')
producer = pycpdf.getProducer(pdf)
prerr()
print(f'producer: {producer}')
print('---cpdf_getCreationDate')
creationDate = pycpdf.getCreationDate(pdf)
prerr()
print(f'creationDate: {creationDate}')
print('---cpdf_getModificationDate')
modificationDate = pycpdf.getModificationDate(pdf)
prerr()
print(f'modificationDate: {modificationDate}')
print('---cpdf_getTitleXMP')
titleXMP = pycpdf.getTitleXMP(pdf)
prerr()
print(f'titleXMP: {titleXMP}')
print('---cpdf_getAuthorXMP')
authorXMP = pycpdf.getAuthorXMP(pdf)
prerr()
print(f'authorXMP: {authorXMP}')
print('---cpdf_getSubjectXMP')
subjectXMP = pycpdf.getSubjectXMP(pdf)
prerr()
print(f'subjectXMP: {subjectXMP}')
print('---cpdf_getKeywordsXMP')
keywordsXMP = pycpdf.getKeywordsXMP(pdf)
prerr()
print(f'keywordsXMP: {keywordsXMP}')
print('---cpdf_getCreatorXMP')
creatorXMP = pycpdf.getCreatorXMP(pdf)
prerr()
print(f'creatorXMP: {creatorXMP}')
print('---cpdf_getProducerXMP')
producerXMP = pycpdf.getProducerXMP(pdf)
prerr()
print(f'producerXMP: {producerXMP}')
print('---cpdf_getCreationDateXMP')
creationDateXMP = pycpdf.getCreationDateXMP(pdf)
prerr()
print(f'creationDateXMP: {creationDateXMP}')
print('---cpdf_getModificationDate')
modificationDateXMP = pycpdf.getModificationDateXMP(pdf)
prerr()
print(f'modificationDateXMP: {modificationDateXMP}')
print('---cpdf_setTitle')
pycpdf.setTitle(pdf, 'title')
prerr()
print('---cpdf_setAuthor')
pycpdf.setAuthor(pdf, 'author')
prerr()
print('---cpdf_setSubject')
pycpdf.setSubject(pdf, 'subject')
prerr()
print('---cpdf_setKeywords')
pycpdf.setKeywords(pdf, 'keywords')
prerr()
print('---cpdf_setCreator')
pycpdf.setCreator(pdf, 'creator')
prerr()
print('---cpdf_setProducer')
pycpdf.setProducer(pdf, 'producer')
prerr()
print('---cpdf_setCreationDate')
pycpdf.setCreationDate(pdf, 'now')
prerr()
print('---cpdf_setModificationDate')
pycpdf.setModificationDate(pdf, 'now')
prerr()
print('---cpdf_setTitleXMP')
pycpdf.setTitleXMP(pdf, 'title')
prerr()
print('---cpdf_setAuthorXMP')
pycpdf.setAuthorXMP(pdf, 'author')
prerr()
print('---cpdf_setSubjectXMP')
pycpdf.setSubjectXMP(pdf, 'subject')
prerr()
print('---cpdf_setKeywordsXMP')
pycpdf.setKeywordsXMP(pdf, 'keywords')
prerr()
print('---cpdf_setCreatorXMP')
pycpdf.setCreatorXMP(pdf, 'creator')
prerr()
print('---cpdf_setProducerXMP')
pycpdf.setProducerXMP(pdf, 'producer')
prerr()
print('---cpdf_setCreationDateXMP')
pycpdf.setCreationDateXMP(pdf, 'now')
prerr()
print('---cpdf_setModificationDateXMP')
pycpdf.setModificationDateXMP(pdf, 'now')
prerr()
try:
  print('---cpdf_getDateComponents')
  components = pycpdf.getDateComponents('now')
  print('---cpdf_dateStringOfComponents')
  dateString = pycpdf.dateStringOfComponents(components)
except:
  prerr()
print('---cpdf_getPageRotation')
rot = pycpdf.getPageRotation(pdf, 1)
prerr()
print('---cpdf_hasBox')
hasBox = pycpdf.hasBox(pdf, 1, '/TrimBox')
prerr()
print('---cpdf_getMediaBox')
mediaBox = pycpdf.getMediaBox(pdf, 1)
prerr()
print(mediaBox)
print('---cpdf_getCropBox')
cropBox = pycpdf.getCropBox(pdf, 1)
prerr()
print(cropBox)
print('---cpdf_getTrimBox')
trimBox = pycpdf.getTrimBox(pdf, 1)
prerr()
print(trimBox)
print('---cpdf_getArtBox')
artBox = pycpdf.getArtBox(pdf, 1)
prerr()
print(artBox)
print('---cpdf_getBleedBox')
bleedBox = pycpdf.getBleedBox(pdf, 1)
prerr()
print(bleedBox)
print('---cpdf_setMediaBox')
pycpdf.setMediaBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
prerr()
print('---cpdf_setCropBox')
pycpdf.setCropBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
prerr()
print('---cpdf_setTrimBox')
pycpdf.setTrimBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
prerr()
print('---cpdf_setArtBox')
pycpdf.setArtBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
prerr()
print('---cpdf_setBleedBox')
pycpdf.setBleedBox(pdf, 1, 1.0, 1.0, 200.0, 200.0)
prerr()
print('---cpdf_markTrapped')
pycpdf.markTrapped(pdf)
prerr()
print('---cpdf_markUntrapped')
pycpdf.markUntrapped(pdf)
prerr()
print('---cpdf_markTrappedXMP')
pycpdf.markTrappedXMP(pdf)
prerr()
print('---cpdf_markUntrappedXMP')
pycpdf.markUntrappedXMP(pdf)
prerr()
print('---cpdf_setPageLayout')
pycpdf.setPageLayout(pdf, pycpdf.singlePage)
prerr()
print('---cpdf_setPageMode')
pycpdf.setPageMode(pdf, pycpdf.useThumbs)
prerr()
print('---cpdf_hideToolbar')
pycpdf.hideToolbar(pdf, True)
prerr()
print('---cpdf_hideMenubar')
pycpdf.hideMenubar(pdf, False)
prerr()
print('---cpdf_hideWindowUi')
pycpdf.hideWindowUi(pdf, True)
prerr()
print('---cpdf_fitWindow')
pycpdf.fitWindow(pdf, True)
prerr()
print('---cpdf_centerWindow')
pycpdf.centerWindow(pdf, True)
prerr()
print('---cpdf_displayDocTitle')
pycpdf.displayDocTitle(pdf, True)
prerr()
print('---cpdf_openAtPage')
pycpdf.openAtPage(pdf, True, 5)
prerr()
print('---cpdf_setMetadataFromFile')
pycpdf.setMetadataFromFile(pdf, 'testinputs/metadata.txt')
prerr()
print('---cpdf_setMetadataFromByteArray')
pycpdf.setMetadataFromByteArray(pdf, 'data')
prerr()
print('---cpdf_getMetadata')
metadata = pycpdf.getMetadata(pdf)
prerr()
print('---cpdf_removeMetadata')
pycpdf.removeMetadata(pdf)
prerr()
print('---cpdf_createMetadata')
pycpdf.createMetadata(pdf)
prerr()
print('---cpdf_setMetadataDate')
pycpdf.setMetadataDate(pdf, 'now')
prerr()
print('---cpdf_getPageLabels')
labels = pycpdf.getPageLabels(pdf)
prerr()
print(labels)
print('---cpdf_addPageLabels')
pycpdf.addPageLabels(pdf, (pycpdf.decimalArabic, "PRE-", 1, pycpdf.all(pdf)), False)
prerr()
print('---cpdf_removePageLabels')
pycpdf.removePageLabels(pdf)
prerr()
print('---cpdf_getPageLabelStringForPage')
labelString = pycpdf.getPageLabelStringForPage(pdf, 1)
prerr()

# CHAPTER 12. File Attachments
print('---cpdf_attachFile')
pycpdf.attachFile('testinputs/attach.txt', pdf)
prerr()
print('---cpdf_attachFileToPage')
pycpdf.attachFileToPage('testinputs/attach.txt', pdf, 1)
prerr()
print('---cpdf_attachFileFromMemory')
pycpdf.attachFileFromMemory('data', 'filename.txt', pdf)
prerr()
print('---cpdf_attachFileToPageFromMemory')
pycpdf.attachFileToPageFromMemory('data', 'filename.txt', pdf, 1)
prerr()
print('---cpdf_removeAttachedFiles')
pycpdf.removeAttachedFiles(pdf)
prerr()
print('---cpdf_getAttachments')
attachments = pycpdf.getAttachments(pdf)
prerr()

# CHAPTER 13. Images
print('---cpdf_getImageResolution')
images = pycpdf.getImageResolution(pdf, 300)
prerr()
print(images)

# CHAPTER 14. Fonts
print('---cpdf_getFontInfo')
fonts = pycpdf.getFontInfo(pdf)
prerr()
print(fonts)
print('---cpdf_removeFonts')
pycpdf.removeFonts(pdf)
prerr()
print('---cpdf_copyFont')
pycpdf.copyFont(pdf, pdf2, r, 1, "/Font")
prerr()

# CHAPTER 15. Miscellaneous
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print('---cpdf_draft')
pycpdf.draft(pdf, r, True)
prerr()
print('---cpdf_removeAllText')
pycpdf.removeAllText(pdf, r)
prerr()
print('---cpdf_blackText')
pycpdf.blackText(pdf, r)
prerr()
print('---cpdf_blackLines')
pycpdf.blackLines(pdf, r)
prerr()
print('---cpdf_blackFills')
pycpdf.blackFills(pdf, r)
prerr()
print('---cpdf_thinLines')
pycpdf.thinLines(pdf, r, 2.0)
prerr()
print('---cpdf_copyId')
pycpdf.copyId(pdf, pdf2)
prerr()
print('---cpdf_removeId')
pycpdf.removeId(pdf)
prerr()
print('---cpdf_setVersion')
pycpdf.setVersion(pdf, 6)
prerr()
print('---cpdf_removeDictEntry')
pycpdf.removeDictEntry(pdf, '/Key')
prerr()
print('---cpdf_removeClipping')
pycpdf.removeClipping(pdf, pycpdf.all(pdf))
prerr()
pycpdf.toFile(pdf, 'testoutputs/squeezed.pdf', False, False)

# CHAPTER 16. (Undocumented or to come in v2.4)
pdf = pycpdf.fromFile('testinputs/cpdfmanual.pdf', '')
print('---cpdf_addContent')
pycpdf.addContent('content', True, pdf, pycpdf.all(pdf))
prerr()
print('---cpdf_outputJSON')
pycpdf.outputJSON('testoutputs/filename.txt', True, False, pdf)
prerr()
print('---cpdf_OCGCoalesce')
pycpdf.OCGCoalesce(pdf)
prerr()
print('---cpdf_OCGRename')
pycpdf.OCGRename(pdf, 'one', 'two')
prerr()
print('---cpdf_OCGOrderAll')
pycpdf.OCGOrderAll(pdf)
prerr()
print('---cpdf_stampAsXObject')
name = pycpdf.stampAsXObject(pdf, pycpdf.all(pdf), pdf2)
prerr()
print('---cpdf_setDemo')
pycpdf.setDemo(True)
prerr()
