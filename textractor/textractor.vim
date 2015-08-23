let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
let NERDTreeMapPreviewSplit = "gi"
let NERDTreeMapCloseChildren = "X"
let Tlist_Sort_Type = "order"
let NERDTreeShowHidden = "0"
let Tlist_Display_Tag_Scope =  1 
let Tlist_Enable_Fold_Column =  1 
let Tlist_Use_SingleClick =  0 
let NERDTreeMapCloseDir = "x"
let NERDTreeSortHiddenFirst = "1"
let Tlist_Show_One_File =  0 
let Tlist_Auto_Highlight_Tag =  1 
let NERDUsePlaceHolders = "1"
let Tlist_Compact_Format =  0 
let UltiSnipsExpandTrigger = "<C-@>"
let NERDTreeMapOpenInTabSilent = "T"
let NERDTreeAutoDeleteBuffer =  0 
let NERDTreeMapRefresh = "r"
let Tlist_Use_Horiz_Window =  0 
let NERDTreeBookmarksFile = "/home/tipishev/.NERDTreeBookmarks"
let UltiSnipsJumpForwardTrigger = "<C-%>"
let NERDTreeMapToggleHidden = "I"
let NERDTreeWinSize = "31"
let Tlist_Ctags_Cmd = "ctags"
let NERDTreeMapRefreshRoot = "R"
let Tlist_Process_File_Always =  0 
let NERDTreeMapPreview = "go"
let UltiSnipsRemoveSelectModeMappings =  1 
let Taboo_tabs = ""
let NERDLPlace = "[>"
let NERDTreeMapActivateNode = "o"
let NERDTreeWinPos = "left"
let NERDTreeMapMenu = "m"
let NERDTreeStatusline = "%{exists('b:NERDTreeRoot')?b:NERDTreeRoot.path.str():''}"
let NERDTreeMapHelp = "?"
let NERDTreeMapJumpParent = "p"
let NERDTreeMapToggleFilters = "f"
let NERDTreeAutoCenter = "1"
let TagList_title = "__Tag_List__"
let NERDTreeShowBookmarks = "0"
let NERDTreeMapJumpPrevSibling = "<C-k>"
let NERDMenuMode = "3"
let NERDDefaultNesting = "1"
let NERDTreeMouseMode = "1"
let NERDTreeRemoveDirCmd = "rm -rf "
let NERDTreeChDirMode = "0"
let Tlist_Highlight_Tag_On_BufEnter =  1 
let NERDTreeMinimalUI = "0"
let NERDTreeAutoCenterThreshold = "3"
let NERDCreateDefaultMappings = "1"
let NERDTreeMapOpenSplit = "i"
let NERDTreeCaseSensitiveSort = "0"
let NERDTreeHijackNetrw = "1"
let Tlist_Max_Submenu_Items =  20 
let NERDTreeShowLineNumbers = "0"
let NERDTreeBookmarksSort = "1"
let NERDTreeHighlightCursorline = "1"
let Tlist_GainFocus_On_ToggleOpen =  0 
let NERDTreeMapOpenInTab = "t"
let Tlist_WinHeight =  10 
let Tlist_Inc_Winwidth =  1 
let NERDTreeRespectWildIgnore = "0"
let Tlist_Auto_Update =  1 
let NERDTreeMapCWD = "CD"
let UltiSnipsEnableSnipMate =  1 
let NERDTreeMapPreviewVSplit = "gs"
let NERDTreeNotificationThreshold = "100"
let NERDTreeMapJumpRoot = "P"
let NERDCommentWholeLinesInVMode = "0"
let UltiSnipsJumpBackwardTrigger = "<c-k>"
let NERDTreeMapChdir = "cd"
let NERDRPlace = "<]"
let Tlist_Exit_OnlyWindow =  0 
let NERDTreeMapToggleZoom = "A"
let UltiSnipsSnippetsDir = "~/.vim/UltiSnips"
let Tlist_Display_Prototype =  0 
let NERDRemoveExtraSpaces = "0"
let Tlist_Max_Tag_Length =  10 
let NERDRemoveAltComs = "1"
let NERDTreeMapJumpLastChild = "J"
let NERDTreeCascadeOpenSingleChildDir = "1"
let NERDTreeMapOpenVSplit = "s"
let Tlist_WinWidth =  30 
let NERDTreeMapDeleteBookmark = "D"
let UltiSnipsListSnippets = "<c-tab>"
let NERDBlockComIgnoreEmpty = "0"
let Tlist_Close_On_Select =  0 
let NERDTreeMapJumpNextSibling = "<C-j>"
let Tlist_File_Fold_Auto_Close =  0 
let Tlist_Auto_Open =  0 
let NERDTreeShowFiles = "1"
let NERDSpaceDelims = "0"
let UltiSnipsEditSplit = "horizontal"
let NERDTreeCopyCmd = "cp -r "
let NERDTreeMapQuit = "q"
let NERDTreeMapChangeRoot = "C"
let NERDCompactSexyComs = "0"
let NERDTreeSortDirs = "1"
let NERDTreeMapToggleFiles = "F"
let NERDAllowAnyVisualDelims = "1"
let NERDTreeDirArrows = "1"
let NERDTreeMapOpenExpl = "e"
let NERDTreeMapJumpFirstChild = "K"
let NERDTreeMapOpenRecursively = "O"
let NERDTreeMapToggleBookmarks = "B"
let NERDTreeMapUpdir = "u"
let NERDTreeMapUpdirKeepOpen = "U"
let NERDTreeQuitOnOpen = "0"
let Tlist_Show_Menu =  0 
let Tlist_Use_Right_Window =  0 
silent only
cd ~/Desktop/Tensor/textractor
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 textractor.py
badd +2 ./utils.py
badd +1 ./main.py
badd +111 ./sources/gazeta
badd +1 out.txt
badd +260 ./sources/slashdot
badd +3 ./sources/slon
badd +1 ./sources/lenta
badd +229 ./sources/meduza
badd +9 ./config.py
badd +1 ~/.vim/UltiSnips/python.snippets
args textractor.py
edit ./main.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 28 + 68) / 136)
exe '2resize ' . ((&lines * 36 + 19) / 39)
exe 'vert 2resize ' . ((&columns * 107 + 68) / 136)
exe '3resize ' . ((&lines * 0 + 19) / 39)
exe 'vert 3resize ' . ((&columns * 107 + 68) / 136)
argglobal
enew
file __Tag_List__
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=9999
setlocal fml=0
setlocal fdn=20
setlocal fen
wincmd w
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
let s:l = 8 - ((7 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
8
normal! 020|
wincmd w
argglobal
edit ./sources/lenta
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
let s:l = 1 - ((0 * winheight(0) + 0) / 0)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 28 + 68) / 136)
exe '2resize ' . ((&lines * 36 + 19) / 39)
exe 'vert 2resize ' . ((&columns * 107 + 68) / 136)
exe '3resize ' . ((&lines * 0 + 19) / 39)
exe 'vert 3resize ' . ((&columns * 107 + 68) / 136)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
