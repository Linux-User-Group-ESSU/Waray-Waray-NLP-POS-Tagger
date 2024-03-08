package com.shirozo.warayTagger

import android.annotation.SuppressLint
import android.app.Dialog
import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.nfc.Tag
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.AttributeSet
import android.view.Gravity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.ViewGroup
import android.view.inputmethod.InputMethodManager
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.appcompat.widget.AppCompatTextView
import androidx.core.content.ContextCompat
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform

class MainActivity : AppCompatActivity() {

    private var  que = 0
    private lateinit var callMain : PyObject
    private lateinit  var scrollV : ScrollView
    private lateinit var scrollLayout : LinearLayout
    private lateinit var prompt : EditText
    private lateinit var Tagdialog : Dialog
    private lateinit var Aboutdialog: Dialog
    @SuppressLint("UseCompatLoadingForDrawables")
    @RequiresApi(Build.VERSION_CODES.Q)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        if (! Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }

        val toolbar = findViewById<androidx.appcompat.widget.Toolbar>(R.id.toolbar)
        setSupportActionBar(toolbar)

        val submit = findViewById<Button>(R.id.submit)

        Tagdialog = Dialog(this)
        Tagdialog.setContentView(R.layout.tags)
        Tagdialog.window?.setLayout(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT)
        Tagdialog.window?.setBackgroundDrawable(getDrawable(R.drawable.input))
        Tagdialog.setCancelable(true)

        Aboutdialog = Dialog(this)
        Aboutdialog.setContentView((R.layout.about))
        Aboutdialog.window?.setLayout(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT)
        Aboutdialog.window?.setBackgroundDrawable(getDrawable(R.drawable.input))
        Tagdialog.setCancelable(true)

        scrollV = findViewById(R.id.scroll)
        scrollLayout = findViewById(R.id.scrollLayout)
        prompt = findViewById(R.id.prompt)

        val py : Python = Python.getInstance()
        val  main = py.getModule("main")
        callMain = main["tag"]!!

        submit.setOnClickListener {
            tag()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.main_menu, menu)
        return true
        //From youtube: Android Knowledge
    }

    @RequiresApi(Build.VERSION_CODES.Q)
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.about -> {
                Aboutdialog.show()
            }
            R.id.tagLabel -> {
                Tagdialog.show()
            }
            R.id.restart -> {
                scrollLayout.removeAllViews()
                val image = findViewById<ImageView>(R.id.logo)
                image.visibility = View.VISIBLE
            }
        }
        return true
        //From youtube: Android Knowledge
    }

    @RequiresApi(Build.VERSION_CODES.Q)
    private fun tag() {
        val image = findViewById<ImageView>(R.id.logo)
        val text = prompt.text.toString()
        prompt.setText("")
        que ++
        if (que >= 1 && text.isNotEmpty()) {
            image.visibility = View.GONE
            val data = callMain.call(text)
            renderTag(data)
        }
        else {
            if (que == 0) {
                image.visibility = View.VISIBLE
            }
        }
    }


    @RequiresApi(Build.VERSION_CODES.Q)
    private fun renderTag(tagset : PyObject) {
        var wordtext = ""
        val wordTags = tagset.asList()
        if(wordTags.size >= 1) {
            for (wordTag in wordTags) {
                val word = wordTag.asList()[0]
                val tag = wordTag.asList()[1]

                wordtext += "$word | $tag   "
            }

            val newLinearLayout = LinearLayout(this)
            val newLinearlayoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
            newLinearlayoutParams.setMargins(0, 0, 0, 20)
            newLinearLayout.layoutParams = newLinearlayoutParams
            newLinearLayout.orientation = LinearLayout.VERTICAL
            newLinearLayout.background = ContextCompat.getDrawable(this, R.drawable.wordtag)

            val newTextView = TextView(this)
            newTextView.layoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WRAP_CONTENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
            newTextView.setTextColor(Color.BLACK)
            newTextView.text = wordtext
            newTextView.setPadding(20, 20, 20, 20)

            val button = Button(this)
            val buttonLayoutParams = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.WRAP_CONTENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
            button.text = "Copy"
            buttonLayoutParams.gravity = Gravity.END
            buttonLayoutParams.setMargins(0, 0, 30, 25)
            button.layoutParams = buttonLayoutParams
            button.setTextColor(ContextCompat.getColor(this, R.color.black))
            button.background = ContextCompat.getDrawable(this, R.drawable.whitebutton)
            button.setOnClickListener {
                val textData = newTextView.text.toString()
                val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
                val clipData = ClipData.newPlainText("text", textData)
                clipboard.setPrimaryClip(clipData)
                Toast.makeText(this, "Text Copied!", Toast.LENGTH_SHORT).show()
            }

            newLinearLayout.addView(newTextView)
            newLinearLayout.addView(button)

            scrollLayout.addView(newLinearLayout)
            scrollV.post { scrollV.fullScroll(View.FOCUS_DOWN) }
        }
    }

}

